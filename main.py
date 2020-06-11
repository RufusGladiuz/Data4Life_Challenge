import csv
import os
import asyncio

async def sendMail(email):
    await asyncio.sleep(.5)
    print("Send mail to {0}".format(email))

async def main():
    tasks = []
    dataPath = os.path.join(os.path.dirname(__file__), "assets", "mails.csv")
    mailCounter = 0
    with open(file = dataPath) as csvfile:

        mails = csv.reader(csvfile, delimiter = ",")

        for row in mails:
            mailCounter += 1
            tasks.append(asyncio.ensure_future(sendMail(row[0])))

    await asyncio.gather(*tasks)
    print("Mails send: " + str(mailCounter))



loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
