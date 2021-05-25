from AvailableSlot import AvailableSlot
import json
import requests
import time

class SlotFinder:

    #AvailableSlots = []
    DistrictId = 0
    RecepientEMails = ""
    SenderEmail = ""
    SenderEmailPasswd = ""
    SMTPServer = ""
    SMTPPort = 0
    DistrictName = ""
    AvailableSlotsObj = []

    def __init__(self, senderEmail, senderEmailPasswd, smtpServer, smtpPort, districtId, recepientemail, dose, districtName):
        
        self.DistrictId = districtId
        self.RecepientEMails = recepientemail
        self.Dose=dose
        self.DistrictName = districtName
        
    def isAvailable (self, centerId, hospitalName, pinCode, minAgeLimit, date, vaccine, availableCapacity, availableCapacityDose1, availableCapacityDose2):
        if (minAgeLimit < 45):
            if ((self.Dose==1) and (availableCapacityDose1 > 0)):
                availSlotObj = AvailableSlot(centerId, hospitalName, pinCode, minAgeLimit, date, vaccine, availableCapacity, availableCapacityDose1, availableCapacityDose2)
                for availSlotObj in self.AvailableSlotsObj:
                    if (availSlotObj.CenterId == centerId and availSlotObj.Date == date):
                        print ("Already there in the list")
                        return
                self.AvailableSlotsObj.append(availSlotObj)
                #self.AvailableSlots.append ({'name' :hospitalName, 'pincode' :pinCode, 'date' :date, 'min_age_limit' :minAgeLimit, 'available_capacity' :availableCapacity, 'available_capacity_dose1': availableCapacityDose1, 'available_capacity_dose2': availableCapacityDose2})
            elif ((self.Dose==2) and (availableCapacityDose2 > 0)):
                availSlotObj = AvailableSlot(centerId, hospitalName, pinCode, minAgeLimit, date, vaccine, availableCapacity, availableCapacityDose1, availableCapacityDose2)
                self.AvailableSlotsObj.append(availSlotObj)
                #self.AvailableSlots.append ({'name' :hospitalName, 'pincode' :pinCode, 'date' :date, 'min_age_limit' :minAgeLimit, 'available_capacity' :availableCapacity, 'available_capacity_dose1': availableCapacityDose1, 'available_capacity_dose2': availableCapacityDose2})
        #else:
        #    print ("Center Id: %s does not have slots", centerId)


    def isJSON (self, response):
        try:
            json.loads(response)
            #print ("Is valid json? true")
            return True
        except ValueError as exception:
            print ("Is valid json? false")
            return False

    def parseJSON (self, jsonResponse):
        jsonObj=json.loads(jsonResponse) 
        centers = jsonObj["centers"]
        for center in centers:
            centerId = center["center_id"]
            hospitalName = center["name"]
            pinCode = center["pincode"]
            for session in center["sessions"]:
                minAgeLimit=session["min_age_limit"]
                date=session["date"]
                vaccine=session["vaccine"]
                availableCapacity=session["available_capacity"]
                availableCapacityDose1=session["available_capacity_dose1"]
                availableCapacityDose2=session["available_capacity_dose2"]
                #Check for Availability
                self.isAvailable(centerId, hospitalName, pinCode, minAgeLimit, date, vaccine, availableCapacity, availableCapacityDose1, availableCapacityDose2)

    def parseResponse(self, response):
        isValidJSON = self.isJSON(response)
        if (isValidJSON):
            #print ("Parse JSON")
            self.parseJSON (response)
        else:
            print ("Not a Valid JSON and hence not parsing")

    def getSlots(self, date):
        baseUrl='https://cdn-api.co-vin.in/api'
        appointment='/v2/appointment/sessions/public/calendarByDistrict'
        districtId=self.DistrictId

        url = baseUrl+appointment
        queryParam = {'district_id': districtId, 'date': date}
        header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36', 'Cache-Control' : 'no-cache'}
        appointments = requests.get(url, params=queryParam, headers=header)
        #appointments = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=294&date=15-05-2021&', headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})

        #print("Header: ",appointments.headers['Content-Type'])
        if (appointments.status_code != 200):
            # This means something went wrong.
            #raise ApiError('GET /appointment/ {}'.format(appointments.status_code))
            print ("Error in API Call. Response Code : " + str(appointments.status_code))
        else:
            self.parseResponse(appointments.text)
        
        return self.AvailableSlotsObj
