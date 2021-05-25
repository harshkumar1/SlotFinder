from EMailNotification import EmailNotification
import time
from AvailableSlot import AvailableSlot


class Notification:
    
    AvailableSlotObjs = []
    RecepEMails = ''
    DistrictName = ''

    def getMailContent(self):
        
        emailNotObj = EmailNotification(self.DistrictName)
        #print ('Center Id: ' + str(self.AvailableSlotObjs[0].CenterId))
        for availSlotObj in self.AvailableSlotObjs:
            mailContent = ''
            if not availSlotObj.NotifiedAt:
                #Has not been Notified, so add to mail content and set Notied At
                centerDetails='Center Id: ' + str(availSlotObj.CenterId) + '\nAvailable Date: ' + availSlotObj.Date + '\nHospital Name: ' + availSlotObj.HospitalName + '\nPin Code: ' + str(availSlotObj.PinCode) + '\nVaccine: ' + availSlotObj.Vaccine + '\nTotal Available Capacity: ' + str(availSlotObj.AvailableCapacity) + '\nAvailable Capacity Dose-1: ' + str(availSlotObj.AvailableCapacityDose1) + '\nAvailable Capacity Dose-2: ' + str(availSlotObj.AvailableCapacityDose2) + '\n\n'
                mailContent = mailContent + centerDetails
                #for recepientEmail in self.RecepientEmails:
                for recepientEmail in self.RecepEMails.split(","):
                    emailNotObj.sendEmail(mailContent, recepientEmail)
                availSlotObj.NotifiedAt=str(time.strftime('%d-%m-%Y %H:%M IST', time.localtime()))
            else:
                #Has been notified already
                print ('Already notified so not notifying')
            #availSlotObj.NotifiedAt=str(time.strftime('%d-%m-%Y %H:%M IST', time.localtime()))
            #print ('Center Id: ' + str(availSlotObj.CenterId) + '\nAvailable Date: ' + availSlotObj.Date + '\nHospital Name: ' + availSlotObj.HospitalName + '\nPin Code: ' + str(availSlotObj.PinCode) + '\nVaccine: ' + availSlotObj.Vaccine + '\nTotal Available Capacity' + str(availSlotObj.AvailableCapacity) + '\nAvailable Capacity Dose-1: ' + str(availSlotObj.AvailableCapacityDose1) + '\nAvailable Capacity Dose-2: ' + str(availSlotObj.AvailableCapacityDose2) + '\n\n')

            #mailContent = mailContent + "Center Id: " + availSlotObj.getCenterId

        #mailContent = AvailableSlotObj  
        return
    
    def __init__(self, recepientEmails, districtName):
        self.RecepEMails = recepientEmails
        self.DistrictName = districtName
        return

    def notify (self, availSlotObjs):
        #Not needed to notify given that no slots are available
        self.AvailableSlotObjs = availSlotObjs
        if (len(self.AvailableSlotObjs) == 0):
            return
        
        mail_content=self.getMailContent()
        #print (mail_content)
        #for recepientEmail in self.RecepientEMails.split(","):
            #self.sendEmail(mail_content, recepientEmail)