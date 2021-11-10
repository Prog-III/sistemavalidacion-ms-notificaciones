# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 12:14:51 2021

@author: WOLF
"""
import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from flask import request
from twilio.rest import Client

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/correo")
def enviarCorreo():
    destino = request.args.get("destino")
    asunto = request.args.get("asunto")
    saludo = request.args.get("saludo")
    mensaje = request.args.get("mensaje")
    hashString = request.args.get("hash")
    if hashString == os.environ.get("SECURITY_HASH"):
        message = Mail(
            from_email=os.environ.get("EMAIL_FROM"),
            to_emails=destino,
            #subject=asunto,
            #html_content=mensaje)
            )
            
        message.template_id = os.environ.get("EMAIL_TEMPLATE_ID")
        
        message.dynamic_template_data = {
            'subject': asunto,
            'saludo': saludo,
            'mensaje': mensaje,
        }
        
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print("Enviado")
            return "OK"
        except Exception as e:
            print(e.message)
            return "KO"
    else:
        print("Hash error")
        return "KO"
    
@app.route("/sms")
def enviarSms():
    destino = request.args.get("destino")
    mensaje = request.args.get("mensaje")
    hashString = request.args.get("hash")
    if hashString == os.environ.get("SECURITY_HASH"):
        try:
            account_sid = os.environ['TWILIO_ACCOUNT_SID']
            auth_token = os.environ['TWILIO_AUTH_TOKEN']
            client = Client(account_sid, auth_token)
            
            message = client.messages \
                            .create(
                                 body=mensaje,
                                 from_=os.environ['PHONE_FROM'],
                                 to="+57"+destino
                             )
            
            print(message.sid)
            
            print("Enviado sms")
            return "OK"
        except Exception as e:
            print(e.message)
            return "KO"
    else:
        print("Hash error")
        return "KO"
      
if __name__ == "__main__":
    app.run()
    