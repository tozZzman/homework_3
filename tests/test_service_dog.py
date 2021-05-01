import requests
import pytest
from jsonschema import validate
from schemas import schema_dog_images, schema_dog_one_image


base_url = 'https://dog.ceo/api/breeds/{}'
base_url_2 = 'https://dog.ceo/api/breed/{}'


def test_status_code():
    response = requests.get(url=base_url.format('list/all'))
    assert response.status_code == 200


def test_validate_schema_random_image():
    response = requests.get(url=base_url.format('image/random'))
    validate(instance=response.json(), schema=schema_dog_one_image)


@pytest.mark.parametrize('path, count', [['hound/images', 1000],
                                         ['hound/images/random/2', 2],
                                         ['hound/images/random/500', 500]])
def test_validate_schema_hound_images(path, count):
    response = requests.get(url=base_url_2.format(path))
    schema_dog_images["properties"]['message']["maxItems"] = count
    validate(instance=response.json(), schema=schema_dog_images)


def test_get_list_sub_breeds():
    response = requests.get(url=base_url_2.format('hound/list'))
    assert response.json()['message'] == ["afghan", "basset", "blood", "english", "ibizan", "plott", "walker"]


@pytest.mark.parametrize('path, type_out', [['hound/afghan/images', list],
                                            ['hound/afghan/images/random', str]])
def test_type_sub_breeds_images(path, type_out):
    response = requests.get(url=base_url_2.format(path))
    type_res = response.json()['message']
    assert isinstance(type_res, type_out)
