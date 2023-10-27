# import os
# import requests
#
# GOOGLE_SHEET_NAME = "Flightdeals"
# # sheet_endpoint = os.environ["ENV_SHEETY_ENDPOINT"]
#
# # sheet_endpoint="https://api.sheety.co/06474ec1154350a853dd27cb2721b46c/flightdeals/prices"
#
# base_url="https://api.sheety.co"
# USERNAME="06474ec1154350a853dd27cb2721b46c"
# PROJECT="flightdeals"
# SHEET="users"
# BEARER="fghsjadoijklsahjsajfhlkjg"
#
# # https://api.sheety.co/06474ec1154350a853dd27cb2721b46c/flightdeals/users
#
# endpoint_url = f"/{USERNAME}/{PROJECT}/{SHEET}"
# Url = base_url + endpoint_url
#
# # print(url)
#
#
# def post_new_row(first_name, last_name, email):
#     print(first_name)
#     print(last_name)
#     print(email)
#
#     new_data = {
#         "user": {
#             "First_Name": first_name,
#             "Last_Name": last_name,
#             "Email":email
#
#
#         }
#     }
#
#     print(new_data)
#
#     headers = {
#         "Authorization": f"Bearer {BEARER}",
#         "Content-Type": "application/json",
#     }
#
#     response = requests.post(url="https://api.sheety.co/06474ec1154350a853dd27cb2721b46c/flightdeals/users",headers=headers,
#                  json=new_data
#                  )
#     response.raise_for_status()
#     print(response.content)

import requests
import os

# BEARER = os.getenv("API_Bearer_Sheety_Repl.it")
# USERNAME = os.getenv("API_Username_Sheety")
#
# PROJECT = "flightDealsUsers"
# SHEET = "users"
#
# base_url = "https://api.sheety.co"

def post_new_row(first_name, last_name, email):
    # endpoint_url = f"/{USERNAME}/{PROJECT}/{SHEET}"
    # url = base_url + endpoint_url

    headers = {

        "Content-Type": "application/json",
    }

    body = {
        "user": {
            "First Name": first_name,
            "Last Name": last_name,
            "Email": email,
        }
    }

    response = requests.post(url="https://api.sheety.co/06474ec1154350a853dd27cb2721b46c/flightdeals/users", headers=headers, json=body)
    response.raise_for_status()
    print(response.text)