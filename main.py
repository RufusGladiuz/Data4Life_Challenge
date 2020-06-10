import csv
import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor


def sendMail(email):
    time.sleep(.5)
    print("Send mail to {0}".format(email))

counter = 0
threadList = []

dataPath = os.path.join(r"E:\Projects\Data4life\assets", "mails.csv")

with open(file = dataPath) as csvfile:
    executor = ThreadPoolExecutor(max_workers=150)
    mails = csv.reader(csvfile, delimiter = ",")

    for row in mails:
        executor.submit(sendMail, row[0])

time.sleep(1)
print("Send Mails: "+ str(counter))

