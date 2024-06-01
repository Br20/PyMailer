from flask import  (current_app)
from  sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *

def send(to, subject, content):
    sg = SendGridAPIClient(api_key=current_app.config['SENDGRID_API_KEY'])
    from_email = Email(current_app.config['FROM_EMAIL'])
    to_email = To(to)
    content = Content('text/plain',content)
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response)