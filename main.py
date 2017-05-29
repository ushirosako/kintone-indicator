#-*- coding: utf-8 -*-

import sys
import smtplib
import os
import json
import datetime
import envs
import pykintone
import yaml
from email.mime.text import MIMEText
from email.utils import formatdate

class Indicator:

    # Load setting valeus
    def __init__(self):
        confSetting = open(envs.FILE_SETTING, 'r')
        global ds
        ds = yaml.load(confSetting)
        confSetting.close()

    # Get kintone app records from define information
    def getRecords(self):
        app = pykintone.load(envs.FILE_ACCOUNT).app()
        resp = app.select(ds['app']['query'])
        if not resp.ok:
            print(resp.error)

        return resp.records
    
    # Calculate the numerical value
    def outputCalc(self, title, val1, val2, flg):

        # Numerical decision
        if val1.isdigit():
            val1 = int(val1)
        else:
            val1 = 0
        
        if val2.isdigit():
            val2 = int(val2)
        else:
            val2 = 0

        value = title + ": {:,}".format(val1)
        if flg == True:
            value += " ({:+,}".format(val1 - val2) + ")"

        return value + "\n"
    
    # Set indicators
    def setIndicate(self):
        rs = self.getRecords()

        if len(rs) < 2:
            print("Error: Need to over two records")
            return False

        val = ""
        for i in range(len(rs) -1):
            val += "Between " + rs[i]["Date"]["value"] + " and " + rs[i+1]["Date"]["value"] + "\n"
            val += self.outputCalc("Members", rs[i]["Member"]["value"], rs[i+1]["Member"]["value"], True)
            val += self.outputCalc("PV", rs[i]["PV"]["value"], rs[i+1]["PV"]["value"], False)
            val += self.outputCalc("UU", rs[i]["UU"]["value"], rs[i+1]["UU"]["value"], False)

        print(val)
        return val
        
    # Create mail
    def createMessage(self, body):

        # Check mail settings
        charset = ds['mail']['charset']
        if charset == None:
            print(ds['project']['code'] + "Not found charset")
            return False

        subject = ds['mail']['subject']
        if subject == None:
            print(ds['project']['code'] + "Not found subject")
            return False
        
        from_addr = ds['mail']['from']
        if from_addr == None:
            print(ds['project']['code'] + "Not found from email address")
            return False

        to_addr = ds['mail']['to']
        if to_addr == None:
            print(ds['project']['code'] + "Not found sendemail address")
            return False
        
        if body == "":
            print(ds['project']['code'] + "Not found body messages")
            return False

        dtNow = datetime.datetime.now()
        msg = MIMEText(body, 'plain', charset)
        msg['Subject'] = subject + " on " + datetime.datetime.strftime(dtNow, "%Y-%m-%d")
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Date'] = formatdate(localtime=True)

        return msg
    
    def sendMail(self, msg):
        try:
            # Set in server and port number
            s = smtplib.SMTP(ds['mail']['smtp'], ds['mail']['port'])

            # Authentication port
            if ds['mail']['port'] in [587]:
                s.ehlo()
                s.starttls()
                s.ehlo()

            if ds['mail']['password'] != None:
                s.login(ds['mail']['from'], ds['mail']['password'])

            s.sendmail(ds['mail']['from'], [msg['To']], msg.as_string())
            s.close()

        except Exception as e:
            print(ds['project']['code'] + str(e))

    # Execute function
    def main(self):

        # Sendmail & Update status
        try:
            # Excute indicator
            body = self.setIndicate()
            if body == False:
                raise Exception

            msg = self.createMessage(body)
            if msg == False:
                print(ds['project']['code'] + "Message not found")
                raise Exception

            # Sendmail
            self.sendMail(msg)
            print("Send to mail >>" + msg['To'])

        except Exception as e:
            print(ds['project']['code'] + str(e))

if __name__ == '__main__':
    sm = Indicator()
    sm.main()
