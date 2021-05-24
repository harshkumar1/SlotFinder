import time

class AvailableSlot:
    CenterId=0
    HospitalName=""
    PinCode=""
    MinAgeLimit=0
    Date="" 
    Vaccine=""
    AvailableCapacity=0
    AvailableCapacityDose1=0
    AvailableCapacityDose2=0
    NotifiedAt=""
    LastAvailableAt=""

    def __init__(self, centerId, hospitalName, pinCode,minAgeLimit, date, vaccine, avlCap, avlCapDose1, avlCapDose2):
        self.CenterId=centerId
        self.HospitalName=hospitalName
        self.PinCode=pinCode
        self.MinAgeLimit=minAgeLimit
        self.Date=date
        self.Vaccine=vaccine
        self.AvailableCapacity=avlCap
        self.AvailableCapacityDose1=avlCapDose1
        self.AvailableCapacityDose2=avlCapDose2
        self.LastAvailableAt=str(time.strftime('%d-%m-%Y %H:%M IST', time.localtime()))

    

