import requests
import pytest
from jsonschema import validate
from schemas import schema_jsonplaceholder

base_url = 'https://jsonplaceholder.typicode.com/'


@pytest.mark.parametrize('path, counts', [['posts', 100],
                                          ['comments', 100],
                                          ['albums', 100],
                                          ['photos', 100],
                                          ['todos', 100],
                                          ['users', 100]])
def test_get_posts(path, counts):
    response = requests.get(base_url + 'posts')
    assert len(response.json()) == counts


def test_status_code():
    response = requests.get(base_url + 'posts')
    assert response.status_code == 200


def test_schemas_jsonplaceholder():
    response = requests.get(base_url + 'posts/1')
    validate(instance=response.json(), schema=schema_jsonplaceholder)


@pytest.mark.parametrize('method, path, out', [
    ['POST', 'posts', {'id': 101}],
    ['PUT', 'posts/1', {'id': 1}],
    ['PATCH', 'posts/1', {
        'userId': 1,
        'id': 1,
        'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
        'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit '
                'molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'
    }],
    ['DELETE', 'posts/1', {}]])
def test_methods(method, path, out):
    response = requests.request(method=method, url=base_url + path)
    assert response.json() == out


def test_headers_content_type():
    response = requests.get(base_url + 'posts')
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
