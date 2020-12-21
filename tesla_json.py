#!/usr/env python

from rauth import OAuth2Service
import json


service = OAuth2Service(
 client_id = '81527cff06843c8634fdc09e8ac0abefb46ac849f38fe1e431c2ef2106796384',
 client_secret = 'c7257eb71a564034f9419ee651c7d0e5f7aa6bfbd18bafb5c5c033b093bb2fa3',
 access_token_url = "https://owner-api.teslamotors.com/oauth/token",
 authorize_url = "https://owner-api.teslamotors.com/oauth/token",
 base_url = "https://owner-api.teslamotors.com/",
 )

email = ''
password = ''

data = {"grant_type": "password",
        "client_id": '81527cff06843c8634fdc09e8ac0abefb46ac849f38fe1e431c2ef2106796384',
        "client_secret": 'c7257eb71a564034f9419ee651c7d0e5f7aa6bfbd18bafb5c5c033b093bb2fa3',
        "email": email,
        "password": password}

session = service.get_auth_session(data=data, decoder=json.loads)
access_token = session.access_token
my_session = service.get_session(token=access_token)

#access vehicle
url = 'https://owner-api.teslamotors.com/api/1/vehicles/'
vehicles = my_session.get(url).json()['response'][0]

v_1 = vehicles['id_s'] #safe vehicle id for further actions 

###################
####Preperation####
###################
my_session.post('https://owner-api.teslamotors.com/api/1/vehicles/' + v_1 + '/wake_up')  #Wakeup car for awaiting commands :)

###################
#####GET (Read only)
###################
#
#getcommand = input("enter get request:")
#getcommandurl='https://owner-api.teslamotors.com/api/1/vehicles/' + v_1 + '/%s' %(getcommand)
#
#print('###Requested get command was %s' %(getcommandurl))
#print(my_session.get(getcommandurl).json())
#
###################
####### POST (Writing permissions)
###################
postcommand = input("enter post request:")
postcommandurl='https://owner-api.teslamotors.com/api/1/vehicles/' + v_1 + '/%s' %(postcommand)
print('###Requested post command was %s' %(postcommandurl))
print(my_session.post(postcommandurl))
