import requests
import pytest
from jsonschema import validate
from schemas import schema_brew

base_url = 'https://api.openbrewerydb.org/breweries'


def test_status_code():
    response = requests.get(base_url)
    assert response.status_code == 200


def test_elements_on_the_page_by_default():
    response = requests.get(base_url)
    assert len(response.json()) == 20


@pytest.mark.parametrize('path, count_item', [['?per_page=50', 50],
                                              ['?per_page=1', 1],
                                              ['?per_page=51', 50],
                                              ['?per_page=0', 0]])
def test_per_page_breweries(path, count_item):
    response = requests.get(base_url + path)
    assert len(response.json()) == count_item


@pytest.mark.parametrize('path, state', [['?by_state=ohio', 'Ohio'],
                                         ['?by_state=new_york', 'New York'],
                                         ['?by_state=new%20mexico', 'New Mexico']])
def test_get_by_state_breweries(path, state):
    response = requests.get(base_url + path)
    for item in response.json():
        assert item['state'] == state


def test_validate_schema_breweries():
    response = requests.get(base_url + '?per_page=1')
    validate(instance=response.json(), schema=schema_brew)
