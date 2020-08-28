# -*- coding: utf-8 -*-
#Autor : gustavo_exe

#Pasos para que funcione

#Paso 1
#Registarse en https://www.twilio.com

#Paso 2
#Instalar desde el terminal:
#pip install twilio

#Codificando

from twilio.rest import Client

#Asignas tu CUENTA SID lo encuentras en el tablero de tu cuenta twilio
accountSid = ''

#Asignas tu TOKEN DE AUTENTICACION lo encuentras abajo de la cuenta sid
authToken = ''

client = Client(accountSid,authToken)

fromWhatsappNumber='whatsapp:+14155238886'
toWhatsappNumber ='whatsapp:+50499231428'

#Cuerpo del mensaje
client.messages.create(body = 'Hola, from gustavo_exe',
                        from_= fromWhatsappNumber,
                        to= toWhatsappNumber)
                        