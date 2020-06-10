import csv
import os
import threading
import time



def sendMail(email):
    time.sleep(.5)
    #print("Send mail to {0}".format(email))

counter = 0
threadList = []

dataPath = os.path.join(r"E:\Projects\Data4life\assets", "mails.csv")

with open(file = dataPath) as csvfile:
    mails = csv.reader(csvfile, delimiter = ",")
    for row in mails:
        try:
            counter += 1
            sendMailThread = threading.Thread(target = sendMail, args = (row[0],))
            sendMailThread.start()
            threadList.append(sendMailThread)

        except RuntimeError:
            initalLenght = len(threadList)
            currentLenght = len(threadList)

            while initalLenght <= currentLenght:
                for t in threadList:
                    if not t.is_alive():
                        threadList.remove(t)
                        currentLenght = len(threadList)
            time.sleep(.1)
            print(counter)
            sendMailThread = threading.Thread(target = sendMail, args = (row[0],))
            sendMailThread.start()
            threadList.append(sendMailThread)

time.sleep(1)
print("Send Mails: "+ str(counter))

