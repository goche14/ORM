# ORM
1.books = Book.objects.filter(price__lt=20)
2.books = Book.objects.filter(
    Q(title__icontains="django") &
    Q(rating__gt=4.0)
)
3.books_range = Author.objects.filter(age__range=(25, 40))
4.books = Book.objects.filter(price__gt=50)
5.