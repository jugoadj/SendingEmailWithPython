import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    
    user = "jugodja@gmail.com"
    msg['from'] = user
    password = "ujcsqknmziwjawwo"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

if __name__== '__main__':
    email_alert("envoiyer par un programme python", "HELLO WORD", "adjoudjugo@gmail.com")
    