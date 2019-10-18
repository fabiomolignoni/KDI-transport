# get all stops
# for each stop, ask for all autobus that came the previous day
# for each data, extract just the bus id and the delay

import requests
import json

url = "https://app-tpl.tndigit.it/gtlservice/trips?&stopId={stopId}&type=U&limit=10000&refDateTime=2019-{month}-{day}T00:10:00.151Z"


with open("./tt_delay.txt", "w") as myfile:
    with requests.Session() as s:
        r = json.loads(s.get("https://app-tpl.tndigit.it/gtlservice/stops").text)
        for i in r:
            # print(r.index(i)/len(r))
            string = s.get(url.format(stopId=i["stopId"], day=17, month=10)).text
            if string != "":
                r = json.loads(string)
                for bus in r:
                    myfile.write(
                        str(i["stopId"])
                        + ","
                        + str(bus["tripId"])
                        + ","
                        + str(bus["delay"])
                        + "\n"
                    )
