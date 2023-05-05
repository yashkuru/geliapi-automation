class TestGeliGetSites:

    # Test case to verify that the API returns a successful response
    def test_get_sites(self, api_logger, api_wrapper):
        response = api_wrapper.run_api(api_logger, "GET", "/sites")
        api_logger.info(f"{response.json()}")
        assert response.status_code == 200
        assert len(response.json()) > 0
        # assert len(response.json()) == 10

    # Test case to verify that the API returns a valid JSON response
    def test_get_sites_valid_json(self, api_logger, api_wrapper):
        response = api_wrapper.run_api(api_logger, "GET", "/sites")
        assert isinstance(response.json(), list)

    # Test case to verify that each site in the response has the expected attributes
    def test_get_sites_valid_json_schema(self, api_logger, api_wrapper):
        response = api_wrapper.run_api(api_logger, "GET", "/sites")
        for site in response.json():
            assert "id" in site
            assert "name" in site
            assert "solar_capacity" in site
