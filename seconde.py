import smtplib
import ssl
from email.message import EmailMessage

subject = "Email From Python"
body = "This is a test email form Python!"
sender_email = "jugodja@gmail.com"
receiver_email = "sirasarah03@gmail.com"
password = input("Enter a password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

html = f"""
<html>
    <body>
        <h1 style="color:#red;">{subject}</h1>
        <img src="https://i.pinimg.com/736x/2b/48/ff/2b48ff407f79fc2ba626dc8535314309.jpg" alt="Girl in a jacket">
        <p>{body}</p>
    </body>
</html>
"""

message.add_alternative(html, subtype="html")

context = ssl.create_default_context()

print("Sending Email!")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Success")