## GELI API Automation framework
This project aims at creating an automation framework on top of which required APIs can be automated

### Steps to Run
Install the required pip packages for the project 
> `pip install -r requirements.txt`

Simply run one of the below commands which runs all the pytest scripts under tests folder
Also generates a html report under reports dir
>`pytest -v tests --html=reports/pytest_report.html`

> `python3.8 -m pytest -v tests --html=reports/pytest_report.html`

logs dir will save all the API calls made by the test script

### Bugs
DELETE api doesn't return the correct `total_capacity` Instead of removing a site's solar capacity from total its adding up.

### Bonus Points API
Implement an API to list VPP to SITE mappings. 
```python
@app.route("/vppsites", methods=["GET"])
def get_vppsites():
    if len(vpp_sites) == 0:
        abort(404)
    return jsonify(vpp_sites)
```

### Project structure
- **lib** contains config file to maintain site URL and headers. **run_api** takes care of sending a API call to the given URL
- **tests** dir contains all the automated tests for each API request.
- **logs** dir will automatically be created for every test run.
- **conftest**.py has all the fixtures that can be reused across multiple tests.
- reports