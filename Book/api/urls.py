from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from Book.api import views

router = DefaultRouter()
router.register(r'books', views.BookViewset, basename='book')
router.register(r'reviews', views.ReviewViewset, basename='review')

# Nested routing
books_router = routers.NestedSimpleRouter(router, r'books', lookup='book')
books_router.register(r'reviews', views.ReviewViewset, basename='book-reviews')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(books_router.urls)),
]























# from django.urls import path,include
# from Book.api import views
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('book',views.BookViewset,basename='book')

# router.register('review',views.ReviewViewset,basename='review')

# urlpatterns = [
#     path('',include(router.urls))
# ]


