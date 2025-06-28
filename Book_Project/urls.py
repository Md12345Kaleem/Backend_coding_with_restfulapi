
from django.contrib import admin
from django.urls import path,include
from Book import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Book.api.urls')), 
    path('book_list/',views.book_list,name="book_list"),
    path('book_review/<int:id>/review',views.book_review,name="book_review"),
    path('Post_data/',views.Post_data,name="Post_data"),
]
