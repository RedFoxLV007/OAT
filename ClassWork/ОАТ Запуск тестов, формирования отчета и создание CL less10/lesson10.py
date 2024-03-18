# работа через консоль CD
import requests
import pytest
#
# params
apikey = "23f82659"
s = "matrix"

base_url = "https://www.omdbapi.com/"
# # ------------------------ test-case invalid param @apikey -----------------------#
def test_invalid_apikey():
    apikey = "rrrr"
    url = f"{base_url}?apikey={apikey}&s={s}"
    response = requests.get(url)
    assert response.status_code in range(400, 500)
    assert response.json()['Response'] == "False"

# # ------------------------ test-case invalid param @apikey -----------------------#
def test_apikey():
    # params
    api_key = "23f82659"
    s = "matrix"
    url = f"{base_url}?apikey={apikey}&s={s}"
    response = requests.get(url)
    assert response.status_code in range(200, 400)
    assert response.json()['Response'] == "True"

