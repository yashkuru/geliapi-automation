import requests
import pytest
from lib.config import GELI_URI
import json

# from lib.run_api import APIRunner

import pytest


class TestGeliPostVpp:

    @pytest.mark.parametrize("site_id, vpp_id", [(9, 2)])
    def test_post_vpp(self, api_logger, api_wrapper, get_site_solar_cap, site_id, vpp_id, get_vpp_total_cap):
        # Setup is done in the fixtures
        api_logger.info(f"Setup: site_id {site_id} has solar capacity {get_site_solar_cap}")
        api_logger.info(f"Setup: vpp {vpp_id} has total capacity {get_vpp_total_cap}")

        # Actual test
        payload = {"site_id": site_id}
        response = api_wrapper.run_api(api_logger, "POST", f"/vpps/{vpp_id}/sites", json=payload)
        assert response.status_code == 200

        response = api_wrapper.run_api(api_logger, "GET", f"/vpps/{vpp_id}")
        assert response.status_code == 200
        vpp = response.json()
        assert vpp['total_capacity'] == get_site_solar_cap+get_vpp_total_cap

    # def test_post_vpp_1(self, api_logger, api_wrapper, get_site_solar_cap, site_id, vpp_id, get_vpp_total_cap):
    #     # Setup is done in the fixtures
    #     api_logger.info(f"Setup: site_id {site_id} has solar capacity {get_site_solar_cap}")
    #     api_logger.info(f"Setup: vpp {vpp_id} has total capacity {get_vpp_total_cap}")
    #
    #     # Actual test
    #     payload = {"site_id": site_id}
    #     response = api_wrapper.run_api(api_logger, "POST", f"/vpps/{vpp_id}/sites", json=payload)
    #
    #     if response:
    #         assert response.status_code == 200
    #         response_g = api_wrapper.run_api(api_logger, "GET", f"/vpps/{vpp_id}")
    #         assert response_g.status_code == 200
    #         vpp = response_g.json()
    #         assert vpp['total_capacity'] == get_site_solar_cap+get_vpp_total_cap



