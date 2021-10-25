import pytest
from django.urls import reverse


@pytest.fixture
def get_homepage_response(client):
    url = reverse('home:home')
    return client.get(url)


def test_homepage_status_code(client):
    response = client.get('/')

    assert response.status_code == 200


def test_homepage_status_code_reverse(get_homepage_response):

    assert get_homepage_response.status_code == 200


def test_homepage_template(get_homepage_response):

    assert 'home/home.html' in [x.name for x in get_homepage_response.templates]


def test_homepage_contains_correct_html(get_homepage_response):

    assert 'Profile' in get_homepage_response.content.decode("UTF-8")
