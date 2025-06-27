import pytest
from django.core.cache import cache
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_cache_miss_path():
    cache.clear()
    client = APIClient()
    resp = client.get('/books/')
    assert resp.json() == []
    assert cache.get('books') is not None
