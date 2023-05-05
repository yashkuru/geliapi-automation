import pytest


class TestGeliGetVpp:

    def test_get_vpp(self, api_logger, api_wrapper):
        vpp_id = 2
        response = api_wrapper.run_api(api_logger, "GET", f"/vpps/{vpp_id}")
        if response:
            assert response.status_code == 200
            vpp = response.json()
            assert vpp['id'] == vpp_id

    def test_get_vpp_invalid(self, api_logger, api_wrapper):
        vpp_id = 44
        response = api_wrapper.run_api(api_logger, "GET", f"/vpps/{vpp_id}")
        if response:
            assert response.status_code == 404

    def test_get_vpp_empty(self, api_logger, api_wrapper):
        vpp_id = ''
        response = api_wrapper.run_api(api_logger, "GET", f"/vpps/{vpp_id}")
        if response:
            assert response.status_code == 404

    # def test_get_vpp_params(self, api_logger, api_wrapper):
    #         payload = {'id': 1}
    #         response = api_wrapper.run_api(api_logger, "GET", "/vpps", json=payload)
    #         if response:
    #             assert response.status_code == 200
