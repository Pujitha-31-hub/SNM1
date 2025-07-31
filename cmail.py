import smtplib
from email.message import EmailMessage
def send_mail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465) #creating object for gmail
    server.login('doppalapudipujitha@gmail.com','hupc zacw rwpd ftek')
    msg=EmailMessage() # creating object for EmailMessage to form email format
    msg['FROM']='doppalapudipujitha@gmail.com'
    msg['TO']=to
    msg['SUBJECT']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.close()
