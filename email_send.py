# -*- coding: utf-8 -*-

import smtplib
import sys
import os
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase



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


    def send_simple_email(self, receivers, subject, text):
        
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


    def send_email_with_image_attach(self, receivers, subject, text, file, rename_file_to = ''):
        
        try:
            msg = MIMEMultipart()
            msg['From'] = self.__sender
            msg['To'] = receivers
            msg['subject'] = subject

            if rename_file_to:         
                with open(file, 'rb') as file:
                    msg_file = MIMEImage(file.read(), name = rename_file_to)
                    msg.attach(msg_file)
            else:
                file_name = os.path.basename(file)
                with open(file, 'rb') as file:
                    msg_file = MIMEImage(file.read(), name = file_name)
                    msg.attach(msg_file)
                
            
            self.__smtp.sendmail(self.__sender, receivers, msg.as_string())
            self.__smtp.quit()

        except Exception as e:
            print(e)
            sys.exit()            
        


    def send_email_with_any_attach(self, receivers, subject, text, file, rename_file_to = ''):
            
        try:
            msg = MIMEMultipart()
            msg['From'] = self.__sender
            msg['To'] = receivers
            msg['subject'] = subject

            if rename_file_to:
                extension_file = os.path.basename(file)
                extension_file = extension_file[-1:-4]  
                with open(file, 'rb') as file:
                    msg_file = MIMEBase('application', 'zip', name = rename_file_to)
                    msg_file.set_payload(file.read())
                encoders.encode_base64(msg_file)
                msg.attach(msg_file)

            else:
                file_name = os.path.basename(file)
                extension_file = file_name[-1:-4]
                print(extension_file)
                print(extension_file)
                with open(file, 'rb') as file:
                    msg_file = MIMEBase('application', 'zip', name = file_name)
                    msg_file.set_payload(file.read())
                encoders.encode_base64(msg_file)
                msg.attach(msg_file)
                
        
            self.__smtp.sendmail(self.__sender, receivers, msg.as_string())
            self.__smtp.quit()

        except Exception as e:
            print(e)
            sys.exit()


