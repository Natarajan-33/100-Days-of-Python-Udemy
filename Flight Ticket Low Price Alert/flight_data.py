from datetime import datetime, timedelta
import requests
TEQUILA_API_KEY="hl20qLIPJ3bfGfAZH3uwlIkXGeZTUD87"
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"

# Get current date and future date after 6 months
today = datetime.today().strftime('%d/%m/%Y')
future_date = (datetime.today() + timedelta(days=180)).strftime('%d/%m/%Y')


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date ,stop_overs=0, via_city=""):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stop_overs = stop_overs
        self.via_city =via_city
