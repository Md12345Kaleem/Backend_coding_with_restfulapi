from Book.models import Book,Review
from Book.api.serializers import BookSerializer,ReviewSerializer
from rest_framework import viewsets

class BookViewset(viewsets.ModelViewSet):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

class ReviewViewset(viewsets.ModelViewSet):
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer