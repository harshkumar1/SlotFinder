import time
from SlotFinder import SlotFinder
from Notification import Notification
import sys
import configparser
import datetime

count=0

def usage():
    print ("Usage:\npython3 main.py <DistrictName>\nCurrent Districts Supported = \"BBMP\", \"MUM\", \"JSR\" \n")
    exit(1)

if (len(sys.argv) != 2):
    print ("District Name needed")
    usage()
else:
    districtName=sys.argv[1]
    if (districtName != "MUM" and districtName != "BBMP" and districtName != "JSR" and districtName != "TEST"):
        print ("District %s not supported"%(sys.argv[1]))
        usage()

#print (districtName)
config = configparser.ConfigParser()
config.read('./app-config.ini')

senderEmail=config['SENDER']['EMAIL']
senderPasswd=config['SENDER']['PASSWD']
smtpServer=config['SENDER']['SMTPSERVER']
smtpPort=config['SENDER']['SMTPPORT']

if districtName == "MUM":
    emailAddresses=config['MUMBAI']['EMAILS']
    districtId=config['MUMBAI']['DISTRICTID']
    logFile=config['MUMBAI']['LOGFILE']
    districtName='MUM'
elif (districtName == 'BBMP'):
    emailAddresses=config['BBMP']['EMAILS']
    districtId=config['BBMP']['DISTRICTID']
    logFile=config['BBMP']['LOGFILE']
    districtName='BBMP'
elif (districtName == 'JSR'):
    emailAddresses=config['EAST-SINGBHUM']['EMAILS']
    districtId=config['EAST-SINGBHUM']['DISTRICTID']
    logFile=config['EAST-SINGBHUM']['LOGFILE']
    districtName='JSR'
elif (districtName == 'TEST'):
    emailAddresses=config['TEST']['EMAILS']
    districtId=config['TEST']['DISTRICTID']
    logFile=config['TEST']['LOGFILE']
    districtName='TEST'

#output_file = open(logFile, 'w')
#sys.stdout = output_file

count=0
#while count < 3:
while True:
    count = count + 1 
    print (count, " Run.", "Slots Availability Checked @ " + str(time.strftime('%d-%m-%Y %H:%M IST', time.localtime())))
    slotFndr = SlotFinder(senderEmail, senderPasswd, smtpServer, smtpPort, districtId, emailAddresses, 2, districtName)
    todayDate=str(datetime.datetime.today().strftime ('%d-%m-%Y'))

    day_delta = datetime.timedelta(days=7)
    start_date = datetime.date.today()
    #end_date = start_date + int(config['COMMON']['FETCHDATAWEEKS'])*day_delta
    #print (start_date)
    #print (end_date)
    
    for i in range(int(config['COMMON']['FETCHDATAWEEKS'])):
        queryDate = str((start_date + i*day_delta).strftime ('%d-%m-%Y'))
        print ("\t Querying for next 7 days starting " + queryDate)
        availSlotObj = slotFndr.getSlots(queryDate)
    Notification(emailAddresses, districtName).notify(availSlotObj)
    #slotFndr.notify()
    #exit(0)
    time.sleep(90)
