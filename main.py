import requests
import os
from twilio.rest import Client

OWN_ENDPOINT="https://api.openweathermap.org/data/2.5/forecast"

# These are your personal credentials and put them from Twilio account of yours 
api_key="API KEY"
account_sid="ACCOUNT SID"
auth_token="AUTH TOKEN"

weather_params={
    "lat":25.277685,
    "lon":91.726486,
    "appid":api_key,
    "cnt":4,

}

response=requests.get(OWN_ENDPOINT,params=weather_params)
response.raise_for_status()
weather_data=response.json()

will_rain=False
for hour_data in weather_data["list"]:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain=True
if will_rain:
    client=Client(account_sid,auth_token)
    message=client.messages \
        .create(
            body="Its's going to rain today. Remember to bring an ☂️ ",
            from_="TWILIO PHONE NUMBER",
            to="YOUR PERSONAL PHONE NUMBER"
        )
    print(message.status)