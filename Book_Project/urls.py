"""
URL configuration for Book_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
