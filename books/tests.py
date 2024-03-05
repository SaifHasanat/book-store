from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from .models import Book, Review


class BookTest(TestCase):

    def setUp(self):
        self.user=get_user_model().objects.create(
            username='testuser',
            email='testuser@gmail.com',
            password='testpass'
        )
        self.book = Book.objects.create(
            title='Harry potter',
            author='Harry',
            price='50.00'

        )
        self.review=Review.objects.create(
            book=self.book,
            author=self.user,
            review=' good review'
        )

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}','Harry potter')
        self.assertEqual(f'{self.book.author}','Harry')
        self.assertEqual(f'{self.book.price}','50.00')

    def test_book_list_view(self):
        response=self.client.get(reverse('books_list'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('books/books_list.html')
        self.assertContains(response,'Harry potter')

    def test_book_detail_view(self):
        response=self.client.get(self.book.get_absolute_url())
        no_response=self.client.get('books/1')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,'Harry potter')
        self.assertContains(response,'a good review')
        self.assertTemplateUsed('books/book_detail.html')