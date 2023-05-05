class TestGeliGetVpp:

    # test retrieves information about a valid VPP and checks if correct VPP details are returned.
    def test_get_vpp(self, api_logger, api_wrapper):
        vpp_id = 1
        response = api_wrapper.run_api(api_logger, "GET", f"/vpps/{vpp_id}")
        assert response.status_code == 200
        vpp = response.json()
        assert vpp['id'] == vpp_id
        assert vpp['name'] == "vpp1"
        assert vpp["total_capacity"] == 10000

    # test attempts to retrieve information about an invalid VPP and checks that the response status code is 404.
    def test_get_vpp_invalid(self, api_logger, api_wrapper):
        vpp_id = 44
        response = api_wrapper.run_api(api_logger, "GET", f"/vpps/{vpp_id}")
        assert response.status_code == 404

    # test tries to retrieve information about a VPP with an empty ID and checks that the response status code is 404.
    def test_get_vpp_empty(self, api_logger, api_wrapper):
        vpp_id = ''
        response = api_wrapper.run_api(api_logger, "GET", f"/vpps/{vpp_id}")
        assert response.status_code == 404

    # def test_get_vpp_params(self, api_logger, api_wrapper):
    #         payload = {'id': 1}
    #         response = api_wrapper.run_api(api_logger, "GET", "/vpps", json=payload)
    #         if response:
    #             assert response.status_code == 200
