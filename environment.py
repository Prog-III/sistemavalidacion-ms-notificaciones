# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 13:16:35 2021

@author: WOLF
"""

import os

#OJO CON EL API KEY EN GITHUB
os.environ["SENDGRID_API_KEY"]= "Aqui va la api key de sengrid"
os.environ["SECURITY_HASH"]="LU3RRjfXHvvl"
os.environ["email_from"]="albertmunoz131@gmail.com"
#OJO CON Estos datos en GITHUB
os.environ["TWILIO_ACCOUNT_SID"]="Aqui va la account sid de twilio"
os.environ["TWILIO_AUTH_TOKEN"]="aqui va el auth token de twilio"
os.environ["phone_from"]="aqui va el telefono predeterminado de twilio"