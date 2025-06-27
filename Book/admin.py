from django.contrib import admin
from .models import Book,Review
# Register your models here.

@admin.register(Book)

class BookAdmin(admin.ModelAdmin):
  list_display = ['id','title','author']

@admin.register(Review)

class ReviewAdmin(admin.ModelAdmin):
  list_display = ['id','book','content','rating']