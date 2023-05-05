class TestGeliGetSite:

    # tests the API call with a valid site ID
    def test_get_site(self, api_logger, api_wrapper):
        site_id = 1
        response = api_wrapper.run_api(api_logger, "GET", f"/sites/{site_id}")
        assert response.status_code == 200
        assert response.json()['id'] == site_id
        assert response.json()["name"] == "mysite1"
        assert response.json()["solar_capacity"] == 10000

    # tests the API call with an invalid site ID
    def test_get_site_invalid(self, api_logger, api_wrapper):
        site_id = 111
        response = api_wrapper.run_api(api_logger, "GET", f"/sites/{site_id}")
        assert response.status_code == 404

    # tests the API call with no site ID specified
    def test_get_site_empty(self, api_logger, api_wrapper):
        site_id = None
        response = api_wrapper.run_api(api_logger, "GET", f"/sites/{site_id}")
        assert response.status_code == 404

    # tests the API call with a non-numeric site ID
    def test_get_site_str(self, api_logger, api_wrapper):
        site_id = "abcd"
        response = api_wrapper.run_api(api_logger, "GET", f"/sites/{site_id}")
        assert response.status_code == 404

    # def test_get_site_params(self, api_logger, api_wrapper):
    #     payload = {'id': 1}
    #     response = api_wrapper.run_api(api_logger, "GET", "/sites", params=payload)
    #     assert response.status_code == 200
