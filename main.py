import csv
import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor


def sendMail(email):
    time.sleep(.5)
    print("Send mail to {0}".format(email))

threadList = []

dataPath = os.path.join(os.path.dirname(__file__), "assets", "mails.csv")

print(dataPath)
with open(file = dataPath) as csvfile:
    executor = ThreadPoolExecutor(max_workers=150)
    mails = csv.reader(csvfile, delimiter = ",")

    for row in mails:
        executor.submit(sendMail, row[0])


