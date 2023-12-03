# import requests
# import json


# class DataManager:
#     # This class is responsible for talking to the Google Sheet.
#     def __init__(self, sheet_data, url, headers):
#         self.url = url
#         self.headers = headers
#         self.sheet_data = json.dumps(sheet_data)
#         try:
#             self.response = requests.put(
#                 url=self.url, data=self.sheet_data, headers=self.headers)
#             self.response.raise_for_status()
#         except requests.exceptions.RequestException as e:
#             print(f"An error occurred: {e}")
