import sendgrid,datetime
import csv

'''This script allows you to send personalized emails using an email client called SendGrid. Visit www.brandonongnz.com and look under projects for more information'''

emailList = {}

#grabs all emails from csv file, remember to create one in the same folder! 
with open ("email1.csv", "rU") as emails:
	emailReader = csv.reader(emails, delimiter=',')
	for row in emailReader:
		k, v = row
		emailList[k] = v


#for every person, insert name into subject
for k, v in emailList.items():
	sg = sendgrid.SendGridClient('username', 'password') #username and password for SendGrid Account
	message = sendgrid.Mail()
	message.add_bcc(v) 

	subject = "How is it going, " + str(k) + "!"  
	message.set_subject(subject)

	
	Message = "<p>Hi " + str(k) + ",<br/><br/>Message continues<br/><br/>Best,<br/>Your Name<br/>your personal details</p>"


	message.set_html(Message)
	message.set_from('First_Name Last_Name <your_email@mail.com>')
	status, msg = sg.send(message)


