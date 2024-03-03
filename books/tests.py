from django.test import TestCase, Client
from django.urls import reverse, resolve
from .models import Book

class BookTest(TestCase):

    def setUp(self):
        self.book=Book.objects.create(
            title='Harry potter',
            author='Harry',
            price='50.00'
        )

    def test_create_object(self):
        self.assertEqual(f'{self.book.title}','Harry potter')
        self.assertEqual(f'{self.book.author}','Harry')
        self.assertEqual(f'{self.book.price}','50.00')

    def test_book_list(self):
        response=self.client.get(reverse('books_list'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('books/books_list.html')
        self.assertContains(response,'Harry potter')

    def test_book_detail(self):
        response=self.client.get(self.book.get_absolute_url())
        no_response=self.client.get('books/1')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,'Harry potter')
        self.assertTemplateUsed('books/book_detail.html')