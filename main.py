import email
import csv
import os
import logging
import threading
import time

def sendMail(email):
    time.sleep(.5)
    print("Send mail to {0}".format(email))

threadList = []

dataPath = os.path.join(r"E:\Projects\Data4life\assets", "mails.csv")

with open(file = dataPath) as csvfile:
    mails = csv.reader(csvfile, delimiter = ",")
    for row in mails:
        try:
            sendMailThread = threading.Thread(target = sendMail, args = (row[0],))
            sendMailThread.start()
            threadList.append(sendMailThread)
        except RuntimeError:
            initalLenght = len(threadList)

            while initalLenght >= len(threadList):

                for t in threadList:

                    if not t.is_alive:
                        threadList.remove(t)
                       
            sendMailThread = threading.Thread(target = sendMail, args = (row[0],))
            sendMailThread.start()
            threadList.append(sendMailThread)
            

