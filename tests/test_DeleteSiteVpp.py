import pytest


class TestGeliDeleteVpp:

    # test verifies for a valid delete case - throws assertion error due to a bug in app code
    @pytest.mark.parametrize("site_id, vpp_id", [(6, 2)])
    def test_delete_vpp(self, api_logger, api_wrapper, site_id, get_site_solar_cap, vpp_id, get_vpp_total_cap):
        # Setup is done in the fixtures to get site solar capacity and vpp's total capacity
        api_logger.info(f"Setup: site_id {site_id} has solar capacity {get_site_solar_cap}")
        api_logger.info(f"Setup: vpp {vpp_id} has total capacity {get_vpp_total_cap}")

        # Post a vpp and later use this to run delete API
        payload = {"site_id": site_id}
        response = api_wrapper.run_api(api_logger, "POST", f"/vpps/{vpp_id}/sites", json=payload)
        assert response.status_code == 200

        # Actual test
        response = api_wrapper.run_api(api_logger, "DELETE", f"/vpps/{vpp_id}/sites", json=payload)
        assert response.status_code == 200

        response = api_wrapper.run_api(api_logger, "GET", f"/vpps/{vpp_id}")
        assert response.status_code == 200
        vpp = response.json()
        assert vpp['total_capacity'] == get_vpp_total_cap - get_site_solar_cap, "Delete API returning wrong value"

    # test checks for invalid vpp id
    @pytest.mark.parametrize("site_id, vpp_id", [(8, 45)])
    def test_delete_vpp_invalid_vpp(self, api_logger, api_wrapper, site_id, vpp_id):
        payload = {"site_id": site_id}
        response = api_wrapper.run_api(api_logger, "DELETE", f"/vpps/{vpp_id}/sites", json=payload)
        assert response.status_code == 404, f"Expected 404 because given vpp id is not a valid entry"

    # test checks for invalid site id
    @pytest.mark.parametrize("site_id, vpp_id", [(4, 2)])
    def test_delete_vpp_invalid_site(self, api_logger, api_wrapper, site_id, vpp_id):
        payload = {"site_id": site_id}
        response = api_wrapper.run_api(api_logger, "DELETE", f"/vpps/{vpp_id}/sites", json=payload)
        assert response.status_code == 404, f"Expected 404 because given vpp id is not a valid entry"

    # test checks for invalid json schema
    @pytest.mark.parametrize("site_id, vpp_id", [(4, 2)])
    def test_delete_vpp_invalid_json(self, api_logger, api_wrapper, site_id, vpp_id):
        payload = {"sites_id": site_id}
        response = api_wrapper.run_api(api_logger, "DELETE", f"/vpps/{vpp_id}/sites", json=payload)
        assert response.status_code == 400, f"Expected 400 because given vpp id is not a valid entry"