# -*- coding: utf-8 -*-

import smtplib
import sys


class EmailSend(object):

    def __init__(self, sender, pwd, host = 'smtp.gmail.com', port = 587):

        self.__host = host
        self.__port = 587
        self.__sender = sender
        self.__pwd = pwd

        try: 
            self.__smtp = smtplib.SMTP(self.__host, self.__port)
            self.__smtp.starttls()
            self.__smtp.login(self.__sender, self.__pwd)

        except Exception as e:
            print(e)
            sys.exit()


    def send(self, receivers, subject, text):
        
        try:
            message = "\r\n".join([
            'From: %s' % self.__sender,
            'To: %s' % receivers,
            'Subject: %s' % subject,
            '',
            '%s' % text
            ])

            self.__smtp.sendmail(self.__sender, receivers, message)
            self.__smtp.quit()

        except Exception as e:
            print(e)
            sys.exit()





