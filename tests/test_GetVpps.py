
class TestGeliGetVpps:

    def test_get_vpps(self, api_logger, api_wrapper):
        response = api_wrapper.run_api(api_logger, "GET", "/vpps")
        assert response.status_code == 200
        assert len(response.json()) > 0

