

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
# Sheety Project API. Check your Google sheet name and Sheety endpoint
import os
import requests
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from datetime import datetime, timedelta
from twilio.rest import Client
from notification_manager import NotificationManager


GOOGLE_SHEET_NAME = "Flightdeals"
sheet_endpoint = os.environ["ENV_SHEETY_ENDPOINT"]

TEQUILA_API_KEY=os.environ["TEQUILA_API_KEY"]
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"



From_city_code="LON"



# Sheety Authentication Option 1: No Auth
sheet_response = requests.get(sheet_endpoint)
data=sheet_response.json()
pprint(data)

flight_search = FlightSearch()
data_manager = DataManager()
notification_manager=NotificationManager()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for key, value in data.items():
    for each_city in value:
        if not each_city["iataCode"]:
            iata_code=flight_search.get_iata_code(each_city["city"])
            each_city["iataCode"] = iata_code
            # print(each_city["id"],each_city["iataCode"])

            data_manager.update_destination_codes(each_city["id"],each_city["iataCode"])

pprint(data)

from_ = '+15736484612',
to = '+91***********'
for key, value in data.items():
    for each_city in value:
        flight_data = flight_search.check_flights(From_city_code, each_city["iataCode"],tomorrow,six_month_from_today)
        if flight_data is None:
            continue
        print(f"{flight_data.destination_city}: £{flight_data.price}")

        if each_city["lowestPrice"]>flight_data.price:
            users = data_manager.get_customer_emails()
            emails = [row["email"] for row in users]
            names = [row["firstName"] for row in users]
            print(f"Book the tickets for {flight_data.destination_city}: £{flight_data.price}")
            body=f"Low price alert! Only £{flight_data.price} to fly from {flight_data.origin_city}-{flight_data.origin_airport} to {flight_data.destination_city}-{flight_data.destination_airport} from {flight_data.out_date} to {flight_data.return_date}"

            if flight_data.stop_overs > 0:
                body += f"\n Flight has {flight_data.stop_overs} stop over, via {flight_data.via_city} city"

            notification_manager.send_msg(body,from_,to)
            notification_manager.send_emails()







