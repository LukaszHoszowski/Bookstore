import pytest
from django.urls import reverse


@pytest.fixture
def get_about_response(client):
    url = reverse('static_pages:about')
    return client.get(url)


def test_about_status_code(client):
    response = client.get('/about/')
    assert response.status_code == 200


def test_about_status_code_reverse(get_about_response):
    assert get_about_response.status_code == 200


def test_about_template(get_about_response):
    assert 'static_pages/about.html' in [x.name for x in get_about_response.templates]


def test_about_contains_correct_html(get_about_response):
    assert 'kalafior' in get_about_response.content.decode("UTF-8")
