class TestGeliGetVpps:

    # tests if the GET /vpps API endpoint returns a valid response status code of 200
    def test_get_vpps(self, api_logger, api_wrapper):
        response = api_wrapper.run_api(api_logger, "GET", "/vpps")
        assert response.status_code == 200
        assert len(response.json()) > 0
        # assert len(response.json()) == 2

    # tests if the GET /vpps API endpoint returns a valid JSON response.
    def test_get_vpps_valid_json(self, api_logger, api_wrapper):
        response = api_wrapper.run_api(api_logger, "GET", "/vpps")
        assert isinstance(response.json(), list)

    # tests if returned a valid JSON response with 'id', 'name' and 'total_capacity' keys.
    def test_get_vpps_valid_json_schema(self, api_logger, api_wrapper):
        response = api_wrapper.run_api(api_logger, "GET", "/vpps")
        for site in response.json():
            assert "id" in site
            assert "name" in site
            assert "total_capacity" in site
