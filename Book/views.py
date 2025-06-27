from .models import Book,Review

def book_list(request):
    books = Book.objects.all() 
    for book in books:
      print(book.id, book.title, book.author)
   


def book_review(request, id):
        book_id = id
        book = Book.objects.get(pk=book_id)
        reviews = book.reviews.all()
        for r in reviews:
          print(r.content, r.rating)



def Post_data(request):

  book = Book(title="1984", author="George Orwell")
  book.save() 
  print(book.id)
  review = Review(book=book, content="Disturbing yet brilliant", rating=5)
  review.save()
