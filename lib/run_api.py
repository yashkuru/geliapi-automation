import pytest
import requests
from config import GELI_URI
# from api_logger import APIlogger


class APIRunner:
    def run_api(self, api_logger, http_method, endpoint, params=None,headers=None, json=None, data=None):
        end_url = f"{GELI_URI}{endpoint}"
        try:
            response = requests.request(http_method, end_url, params=params, headers=headers, json=json, data=data)
            print(response)
            print(response.url)
            print(response.json())
            api_logger.info(f"{http_method}{endpoint} {params} {response.status_code} {response.json()}")
            return response
        except requests.exceptions.HTTPError as httperr:
            api_logger.error(f"HTTP Error: {httperr}")
            # pytest.skip(f"Test skipped due to connection setup failed {httperr}")
        except requests.exceptions.ConnectionError as connexc:
            api_logger.error(f"Connection Error: {connexc}")
            pytest.skip(f"Test skipped as connection setup failed {connexc}")
        except Exception as exc:
            api_logger.error(f"Error: {exc.args}")
            # pytest.skip(f"Test skipped as connection setup failed {exc.args}")



