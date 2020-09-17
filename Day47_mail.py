#Sending mails using python
import smtplib
from email.message import EmailMessage

email=EmailMessage()
email['from']='Secret agent'
email['to']='#'
email['subject']='This mail was sent using python!'
email.set_content('This is a auto generated mail!')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('#','#')
    smtp.send_message(email)
    print('task completed')