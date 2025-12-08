# ORM
1.books = Book.objects.filter(price__lt=20)
2.books = Book.objects.filter(
    Q(title__icontains="django") &
    Q(rating__gt=4.0)
)
3.books_range = Author.objects.filter(age__range=(25, 40))
4.books = Book.objects.filter(price__gt=50)
5.Book.objects.exclude(rating=5)
6.Book.objects.filter(Q(title__startswith="A") | Q(title__endswith="Z")).delete()
7.Author.objects.filter(Q(name__icontains="john") | Q(age__gt=60))
8.Book.objects.exclude(price__range=(10, 30)).delete()
9.Book.objects.filter(Q(stock=0) | Q(rating__isnull=True))
10.Author.objects.filter(name__startswith="M", age__lt=30)
11.Book.objects.filter(Q(title__startswith="A") | Q(author__name__icontains="John"))
12.keyword = "ai"
Book.objects.filter(Q(title__icontains=keyword) | Q(author__name__icontains=keyword))
13.Book.objects.filter(
    Q(price__lt=10, rating__lt=3) | Q(price__gt=80)
).delete()
14.Author.objects.filter(
    book__in=Book.objects.filter(Q(price__gt=50) | Q(rating__lt=2))
).distinct()
15.Book.objects.filter(
    Q(published_year=2020) |
    Q(rating__gte=4, stock__lt=5)
).delete()
16.Book.objects.filter(
    Q(author__age__gt=50) | Q(author__age__lt=20)
)
17.Book.objects.filter(
    title__icontains="python",
    rating__isnull=False
).delete()
18.Book.objects.filter(
    title__icontains="AI"
).filter(
    Q(price__lt=30) | Q(stock__gt=20)
)
19.Author.objects.filter(book__isnull=True)
20.Book.objects.filter(
    Q(price__range=(20,40)) | Q(rating__range=(4,5))
).delete()
21.Book.objects.filter(stock__lt=F("price"))
22.Book.objects.update(price=F("price") + 10)
23.Book.objects.filter(rating__gt=4).update(stock=F("stock") - 2)
24.Book.objects.filter(price__gte=F("rating") * 2)
25.Book.objects.update(price=F("price") * 0.9)
26.Book.objects.filter(author__age__gt=F("price"))
27.Book.objects.filter(price__lt=20).update(stock=F("stock") + 5)
28.Book.objects.filter(rating=F("price")).delete()
29.Book.objects.annotate(
    value=F("price") * F("stock")
).filter(value__gt=500)
30.Book.objects.update(
    price=F("rating"),
    rating=F("price")
)
