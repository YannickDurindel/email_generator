#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 13:10:30 2022

@author: yannick
NB : this is a very bold code that requires good wifi connection. 
"""

import yagmail
import time
import time

with open('path/file') as f:
    email = [line for line in f.readlines()]

user = 'your@email'
app_password = 'token' # a token for gmail
subject = 'email title'

content = """
your email
"""

for k in range(320,len(email)):
    to = email[k]
    try :
        if k%10 == 9:
            time.sleep(30)
        with yagmail.SMTP(user, app_password) as yag:
            yag.send(to, subject, content)
            print('Email sent successfully   '+str(round(100*k/len(email),3))+"%")
            k+=1
    except :
        print('sending fail')
        
print("Done !")
