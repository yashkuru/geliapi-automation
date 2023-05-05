
class TestGeliGetSite:

    def test_get_site(self, api_logger, api_wrapper):
        site_id = 1
        response = api_wrapper.run_api(api_logger, "GET", f"/sites/{site_id}")
        if response:
            assert response.status_code == 200
            assert response.json()['id'] == site_id

    def test_get_site_invalid(self, api_logger, api_wrapper):
        site_id = 111
        response = api_wrapper.run_api(api_logger, "GET", f"/sites/{site_id}")
        if response:
            assert response.status_code == 404

    def test_get_site_empty(self, api_logger, api_wrapper):
        site_id = None
        response = api_wrapper.run_api(api_logger, "GET", f"/sites/{site_id}")
        if response:
            assert response.status_code == 404

    # def test_get_site_params(self, api_logger, api_wrapper):
        #     payload = {'id': 1}
        #     response = api_wrapper.run_api(api_logger, "GET", "/sites", params=payload)
        #     if response:
        #         assert response.status_code == 200
