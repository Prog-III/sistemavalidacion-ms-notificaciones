# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 13:16:35 2021

@author: WOLF
"""

import os

#OJO CON EL API KEY EN GITHUB
os.environ["SENDGRID_API_KEY"]= "APIKEYSENDGRID"
os.environ["SECURITY_HASH"]="hashseguridad"
os.environ["email_from"]="CorreoFrom"
os.environ["Correo-TemplateID"]="IdTemplate"
#OJO CON Estos datos en GITHUB
os.environ["TWILIO_ACCOUNT_SID"]="TWILISID"
os.environ["TWILIO_AUTH_TOKEN"]="TWILIOTOKEN"
os.environ["phone_from"]="PHONEFROM"
