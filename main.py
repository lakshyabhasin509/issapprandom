import time
import smtplib
import requests
from datetime import datetime


MY_EMAIL="lakshyabhasinissnfo@gmail.com"
MY_PASSWORD="kjwphedmccmqsvlj"
MY_LATS=30.316496
MY_LONGS=78.032188


def is_iss_inPosition():
    response=requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status();
    data=response.json()

    iss_longitude=float(data["iss_position"]["longitude"])
    iss_latitude=float(data["iss_position"]["latitude"])

    if MY_LATS-5 <= iss_latitude <=MY_LATS+5 and MY_LONGS-5 <=iss_longitude <=MY_LONGS+5:
        return True
    else:
        return False

def is_night():
    parameters={
        "lat":MY_LATS,
        "lng":MY_LONGS,
        "formatted" : 0
    }

    resp=requests.get(url='http://api.sunrise-sunset.org/json',params=parameters)
    resp.raise_for_status()

    data=resp.json()

    sunrise=data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset=data["results"]["sunset"].split("T")[1].split(":")[0]
    print(sunrise)
    print(sunset)

    time_now=datetime.now().hour

    if time_now>=sunset and time_now<=sunrise:
        return True

while True:
    time.sleep(3)
    if True:
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject: Look up its Hereee!!!!\n\n International space startion is just above you")
        connection.close()

