import os
import requests

GOOGLE_SHEET_NAME = "Flightdeals"
sheet_endpoint = os.environ["ENV_SHEETY_ENDPOINT"]


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        # Initialize with your Sheety project ID and sheet name
        self.sheet_name = "Flightdeals"
        self.customer_data= None


    def update_destination_codes(self, city_id, code):
        new_data = {
            "price": {
                "iataCode": code
            }
        }
        requests.put(url=f"{sheet_endpoint}/{city_id}",
                    json=new_data
                    )

    def get_customer_emails(self):
        customers_endpoint = sheet_endpoint
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data

