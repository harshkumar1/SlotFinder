import smtplib
from email.mime.text import MIMEText
import time
import configparser

class EmailNotification:

    SenderEmail = ''
    SenderEmailPasswd = ''
    SMTPServer = ''
    SMTPPort = ''
    DistrictName = '' 

    def __init__(self, districtName):
        config = configparser.ConfigParser()
        config.read('./app-config.ini')
        self.SenderEmail = config['SENDER']['EMAIL']
        self.SenderEmailPasswd = config['SENDER']['PASSWD']
        self.SMTPServer = config['SENDER']['SMTPSERVER']
        self.SMTPPort = config['SENDER']['SMTPPORT']
        self.DistrictName = districtName
        
    #def createMailContent(self):
     #   mail_content=""
      #  if (len(self.AvailableSlots) == 0):
       #     mail_content = "No slots available now. Will keep you posted.\n"
        #else:
         #   for availableSlot in self.AvailableSlots:
          #      hospitalName = availableSlot["name"]
           #     pinCode = availableSlot["pincode"]
            #    minAgeLimit=availableSlot["min_age_limit"]
             #   date=availableSlot["date"]
              #  availableCapacity=availableSlot["available_capacity"]
               # availableCapacityDose1=availableSlot["available_capacity_dose1"]
                #availableCapacityDose2=availableSlot["available_capacity_dose2"]
                #mail_content=mail_content+"Hospital Name " + str(hospitalName) + "\nPin Code: " + str(pinCode) + "\nDate: " + str(date) + "\nMin Age: " + str(minAgeLimit) + "\n Available Capacity: " + str(availableCapacity) + "\n Available Capacity Dose-1: " + str(availableCapacityDose1) + "\n Available Capacity Dose-2: "+ str(availableCapacityDose2) + "\n\n"
        
        #mail_content=mail_content+"\nSlots Availability Checked @ " + str(time.strftime('%d-%m-%Y %H:%M IST', time.localtime()))
        #return mail_content

    def sendEmail(self, mail_content, recepientEmail):

        sender_address = self.SenderEmail
        receiver_address = recepientEmail
        account_password = self.SenderEmailPasswd
        subject = 'Covid-19 Vaccination Slot Finder [ ' + self.DistrictName + ' ]'
        body = mail_content
        try:
            # Endpoint for the SMTP Gmail server (Don't change this!)
            smtp_server = smtplib.SMTP_SSL(self.SMTPServer, self.SMTPPort)
            # Login with your Gmail account using SMTP
            smtp_server.login(sender_address, account_password)
            # Let's combine the subject and the body onto a single message
            message = f"Subject: {subject}\n\n{body}"
            # We'll be sending this message in the above format (Subject:...\n\nBody)
            smtp_server.sendmail(sender_address, receiver_address, message)
            # Close our endpoint
            smtp_server.close()
        except Exception as e:
            print ('Error while sending email. Exception : ')
            print (e)