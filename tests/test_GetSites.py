
class TestGeliGetSites:

    def test_get_sites(self, api_logger, api_wrapper):
        response = api_wrapper.run_api(api_logger, "GET", "/sites")
        assert response.status_code == 200
        assert len(response.json()) > 0
