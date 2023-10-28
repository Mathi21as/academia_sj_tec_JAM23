from flask_mail import Mail , Message   
from flask import render_template
import os


mailer = Mail()

class EmailManager ():       

    @classmethod
    def sendEmail (self, email):
        msg = Message('Nuevo registro',
                               sender = os.environ.get('MAIL_USERNAME'),
                               recipients= [email])
                
        msg.html = render_template('email.html' , userEmail = email)
        mailer.send(msg)
        print(msg)