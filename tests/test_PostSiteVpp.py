import pytest


class TestGeliPostVpp:

    @pytest.mark.parametrize("site_id, vpp_id", [(9, 2)])
    def test_post_vpp(self, api_logger, api_wrapper, get_site_solar_cap, site_id, vpp_id, get_vpp_total_cap):
        # Setup is done in the fixtures to get site solar capacity and vpp's total capacity
        api_logger.info(f"Setup: site_id {site_id} has solar capacity {get_site_solar_cap}")
        api_logger.info(f"Setup: vpp {vpp_id} has total capacity {get_vpp_total_cap}")

        # Actual test
        payload = {"site_id": site_id}
        response = api_wrapper.run_api(api_logger, "POST", f"/vpps/{vpp_id}/sites", json=payload)
        assert response.status_code == 200

        response = api_wrapper.run_api(api_logger, "GET", f"/vpps/{vpp_id}")
        assert response.status_code == 200
        vpp = response.json()
        assert vpp['total_capacity'] == get_site_solar_cap + get_vpp_total_cap

    @pytest.mark.parametrize("site_id, vpp_id", [(8, 3)])
    def test_post_vpp_invalid_vpp(self, api_logger, api_wrapper, site_id, vpp_id):
        payload = {"site_id": site_id}
        response = api_wrapper.run_api(api_logger, "POST", f"/vpps/{vpp_id}/sites", json=payload)
        if response is not None:
            assert response.status_code == 404, f"Expected 404 because given vpp id is not a valid entry"

    @pytest.mark.parametrize("site_id, vpp_id", [(22, 2)])
    def test_post_vpp_invalid_site(self, api_logger, api_wrapper, site_id, vpp_id):

        payload = {"site_id": site_id}
        response = api_wrapper.run_api(api_logger, "POST", f"/vpps/{vpp_id}/sites", json=payload)
        if response is not None:
            assert response.status_code == 404, f"Expected 404 because given site id is not a valid entry"

    @pytest.mark.parametrize("site_id, vpp_id", [(22, 33)])
    def test_post_vpp_invalid_site_vpp(self, api_logger, api_wrapper, site_id, vpp_id):

        payload = {"site_id": site_id}
        response = api_wrapper.run_api(api_logger, "POST", f"/vpps/{vpp_id}/sites", json=payload)
        if response is not None:
            assert response.status_code == 404, f"Expected 404 because given vpp and site id is not a valid entry"

    @pytest.mark.parametrize("site_id, vpp_id", [(22, 33)])
    def test_post_vpp_invalid_payload(self, api_logger, api_wrapper, site_id, vpp_id):

        payload = {"site_ida": site_id}
        response = api_wrapper.run_api(api_logger, "POST", f"/vpps/{vpp_id}/sites", json=payload)
        if response is not None:
            assert response.status_code == 400, f"Expected 400 because given payload has wrong keyid"

    @pytest.mark.parametrize("site_id, vpp_id", [(3, 2)])
    def test_post_vpp_dup_site(self, api_logger, api_wrapper, site_id, vpp_id):

        payload = {"site_id": site_id}
        response = api_wrapper.run_api(api_logger, "POST", f"/vpps/{vpp_id}/sites", json=payload)
        if response is not None:
            assert response.status_code == 409, f"Expected 409 because given site id is already part of vvp"

