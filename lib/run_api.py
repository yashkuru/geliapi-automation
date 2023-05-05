import pytest
import requests

from config import GELI_URI


class APIRunner:
    @staticmethod
    def run_api(api_logger, http_method, endpoint, params=None, headers=None, json=None, data=None):
        end_url = f"{GELI_URI}{endpoint}"

        # Sending API request using requests library
        try:
            response = requests.request(http_method, end_url, params=params, headers=headers, json=json, data=data)
            api_logger.info(f"{http_method}{endpoint} {params} {response.status_code} {response.reason} {response.url}")
            # api_logger.info(f"{http_method}{endpoint} {params} {response.status_code} {response.json()}")
            return response
        except requests.exceptions.HTTPError as httperr:
            api_logger.error(f"HTTP Error: {httperr}")
        except requests.exceptions.ConnectionError as connexc:
            api_logger.error(f"Connection Error: {connexc}")
            pytest.skip(f"Test skipped as connection setup failed {connexc}")
        except Exception as exc:
            api_logger.error(f"Error: {exc.args} {exc.with_traceback}")
