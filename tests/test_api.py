import json

import pytest
from django.shortcuts import resolve_url
from django.test.client import Client

save_email_url = resolve_url('save_email')


@pytest.fixture
def client(request):
    return Client()


def test_save_email_api_ok(client):
    resp = client.get(save_email_url, {'slug': 'test', 'email': 'test@test.com'})
    assert resp.status_code == 200
    assert resp.json().get('ok')

    from api.models import Email
    assert Email.objects.filter(slug='test', email='test@test.com').first()


def test_save_email_api_missing_param(client):
    resp = client.get(save_email_url, {'email': 'test@test.com'})
    assert resp.status_code == 200
    assert not resp.json().get('ok')

    resp = client.get(save_email_url, {'slug': 'test'})
    assert resp.status_code == 200
    assert not resp.json().get('ok')


def test_save_email_api_wrong_email(client):
    resp = client.get(save_email_url, {'slug': 'test', 'email': 'test@tecom'})
    assert resp.status_code == 200
    assert not resp.json().get('ok')
