import pytest
from rest_framework.test import APIClient
from reviews.models import Book

@pytest.mark.django_db
def test_add_and_list_book():
    client = APIClient()
    resp = client.post('/books/', {'title': 'Test', 'author': 'Author'})
    assert resp.status_code == 201
    resp = client.get('/books/')
    assert resp.status_code == 200
    assert any(b['title'] == 'Test' for b in resp.json())

@pytest.mark.django_db
def test_reviews_404_on_missing_book():
    client = APIClient()
    resp = client.get('/books/999/reviews/')
    assert resp.status_code == 404
