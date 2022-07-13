import requests
import os

class HttpClient:
    def __init__(self):
        self.base_url = 'https://api.nasa.gov/mars-photos/api/v1'
        self.api_key = os.getenv('API_KEY')

    @staticmethod
    def call_api(url, method, query, headers=None):
        """call the specified url with the specified call and paramaters

        Inputs
            url: url endpoint to be called
            params: parameters for the api call
            method: type of call to make to the url

        Raises
            Exception in the case of connection error

        Outputs
            response: json of the response
        """

        try:
            response = requests.request(
                method,
                url,
                headers=headers,
                params=query
            )

            response.raise_for_status()

            return response.json()

        except requests.exceptions.HTTPError as http_err:

            print(f"HTTP error occurred: {http_err}")

        except Exception as err:

            print(f"Error occurred: {err}")


    def get_images(self, rover_name, day=None, is_random=False):
        return self.call_api(f'{self.base_url}/rovers/{rover_name}/photos', 'GET', {'api_key': self.api_key, 'earth_date': day})

    def get_manifest(self, rover_name):
        return self.call_api(f'{self.base_url}/manifests/{rover_name}', 'GET', {'api_key': self.api_key})