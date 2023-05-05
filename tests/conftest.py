import logging
import os
import pytest
from lib.run_api import APIRunner


@pytest.fixture(scope="session")
def api_logger(loglevel="INFO"):
    test_logger = logging.getLogger("geli_api_logger")
    if not os.path.isdir("../logs"):
        os.mkdir("../logs")
    handler = logging.FileHandler("../logs/api_test.log")
    formatter = logging.Formatter("%(asctime)s %(name)-10s %(levelname)-6s %(message)s")
    handler.setFormatter(formatter)
    test_logger.addHandler(handler)

    loglevel = logging.DEBUG if loglevel == "DEBUG" else logging.INFO
    test_logger.setLevel(loglevel)
    return test_logger


@pytest.fixture(scope="session")
def api_wrapper():
    return APIRunner()


@pytest.fixture
def get_site_solar_cap(site_id, api_logger, api_wrapper):
    site_capacity = 0
    print(site_id)
    response = api_wrapper.run_api(api_logger, "GET", f"/sites/{site_id}")
    print("response-si", response)
    print("response-st", response)
    if response is not None:
        site_capacity = response.json()['solar_capacity']
        return site_capacity
    else:
        return response


@pytest.fixture
def get_vpp_total_cap(vpp_id, api_logger, api_wrapper):
    total_capacity = 0
    print(vpp_id)
    response = api_wrapper.run_api(api_logger, "GET", f"/vpps/{vpp_id}")
    if response.json():
        total_capacity = response.json()['total_capacity']
    return total_capacity
