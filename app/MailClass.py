import pyperclip
import requests
import random
import string
import time
import sys
import re
import os


class MailClass:
    def __init__(self):
        #self.name = name
        self.API = 'https://www.1secmail.com/api/v1/'
        self.domainList = ['1secmail.com', '1secmail.net', '1secmail.org']
        self.domain = random.choice(self.domainList)
        self.prefix = self.generateUserName()
        self.mail = self.generateMail()

    def generateUserName(self):
        name = string.ascii_lowercase + string.digits
        username = ''.join(random.choice(name) for i in range(10))
        return username

    def extract(self):
        getUserName = self.prefix
        getDomain = self.domain
        return [getUserName, getDomain]

    def deleteMail(self):
        url = 'https://www.1secmail.com/mailbox'
        data = {
            'action': 'deleteMailbox',
            'login': f'{self.prefix}',
            'domain': f'{self.domain}'
        }

        self.mail = self.prefix + "@" + self.domain

        print("Disposing your email address - " + self.mail + '\n')
        req = requests.post(url, data=data)

    def getMail(self):
        return self.mail

    def generateMail(self):
        self.domain = random.choice(self.domainList)

        newMail = f"{self.API}?login={self.generateUserName()}&domain={self.domain}"
        reqMail = requests.get(newMail)
        self.mail = f"{self.prefix}@{self.domain}"

        print(f"Created new mail {self.mail}")

        return self.mail

    def checkMails(self):
        reqLink = f'{self.API}?action=getMessages&login={self.prefix}&domain={self.domain}'
        req = requests.get(reqLink).json()
        length = len(req)
        if length == 0:
            print("Your mailbox is empty. Hold tight. Mailbox is refreshed automatically every 5 seconds. \n")
        else:
            idList = []
            for i in req:
                for k, v in i.items():
                    if k == 'id':
                        mailId = v
                        idList.append(mailId)

            x = 'mails' if length > 1 else 'mail'
            print(f"You received {length} {x}. (Mailbox is refreshed automatically every 5 seconds.)\n")

            current_directory = os.getcwd()
            final_directory = os.path.join(current_directory, r'All Mails')
            if not os.path.exists(final_directory):
                os.makedirs(final_directory)

            for i in idList:
                msgRead = f'{self.API}?action=readMessage&login={self.prefix}&domain={self.domain}&id={i}'
                req = requests.get(msgRead).json()
                for k, v in req.items():
                    if k == 'from':
                        sender = v
                    if k == 'subject':
                        subject = v
                    if k == 'date':
                        date = v
                    if k == 'textBody':
                        content = v

                mail_file_path = os.path.join(final_directory, f'{i}.txt')

                with open(mail_file_path, 'w') as file:
                    file.write(
                        "Sender: " + sender + '\n' + "To: " + self.mail + '\n' + "Subject: " + subject + '\n' + "Date: " + date + '\n' + "Content: " + content + '\n')
                    return content

            return None
