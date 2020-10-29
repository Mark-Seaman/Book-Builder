from django.test import TestCase

from book.author import add_author, get_author
from book.book import add_book, delete_book, get_book, list_books
from book.models import Book
from book.tests import create_test_user


# -----------------------------------------------------
#   B o o k

class BookTests(TestCase):

    def check_book_author(self, pk, name):
        b = Book.objects.get(pk=pk)
        self.assertEqual(b.author.name, name)

    def check_book_title(self, pk, title):
        b = Book.objects.get(pk=pk)
        self.assertEqual(b.title, title)

    def check_description(self, pk, text):
        b = Book.objects.get(pk=pk)
        self.assertEqual(b.description, text)

    def check_num_books(self, num):
        self.assertEqual(len(list_books()), num)

    def setUp(self):
        self.user = create_test_user()
        author = add_author(self.user, 'Charles Dickens')
        self.book = add_book('Tale of Two Cities', author)

    def test_book_model(self):
        self.check_num_books(1)
        self.check_book_title(1, 'Tale of Two Cities')
        self.check_book_author(1, 'Charles Dickens')

    def test_create_book(self):
        self.check_num_books(1)
        author = get_author('Charles Dickens')
        add_book('Christmas Carol', author)
        self.check_num_books(2)
        self.check_book_title(2, 'Christmas Carol')

    def test_create_author(self):
        jack = add_author(self.user, 'Jack London')
        add_book('Sea Wolf', jack)
        self.check_num_books(2)
        self.check_book_author(2, 'Jack London')
        self.check_book_title(2, 'Sea Wolf')

    def test_list_books(self):
        add_book('Sea Wolf', add_author(self.user, 'Jack London'))
        add_book('1984', add_author(self.user, 'George Orwell'))
        self.check_num_books(3)

    def test_update_book(self):
        self.check_num_books(1)
        a = get_book('Tale of Two Cities')
        a.title = 'Christmas Carol'
        a.save()
        self.check_book_title(1, 'Christmas Carol')
        self.check_book_author(1, 'Charles Dickens')

    def test_description(self):
        self.check_description(1, None)
        a = get_book('Tale of Two Cities')
        a.description = 'This is a book description'
        a.save()
        self.check_description(1, 'This is a book description')

    def test_delete_book(self):
        delete_book('Tale of Two Cities')
        self.check_num_books(0)


# -----------------------------------------------------
#   B o o k    V i e w s

class BookViewsTests(TestCase):

    def setUp(self):
        self.user = create_test_user()
        self.author = add_author(self.user, 'Charles Dickens')
        self.book = add_book('Tale of Two Cities', self.author)

    def test_string_representation(self):
        book = Book.objects.get(pk=1)
        self.assertEqual(str(book), '1 - Tale of Two Cities by Charles Dickens')

    def test_get_absolute_url(self):
        self.assertEqual(self.book.get_absolute_url(), '/book/1')

    def test_book_content(self):
        self.assertEqual(f'{self.book.title}', 'Tale of Two Cities')
        self.assertEqual(f'{self.book.author.name}', 'Charles Dickens')
        self.assertEqual(f'{self.book.description}', 'None')

#    def test_book_list_view(self):
#        response = self.client.get(reverse('home'))
#        self.assertEqual(response.status_code, 200)
#        self.assertContains(response, 'Nice body content')
#        self.assertTemplateUsed(response, 'home.html')
#
#    def test_book_detail_view(self):
#        response = self.client.get('/book/1/')
#        no_response = self.client.get('/book/100000/')
#        self.assertEqual(response.status_code, 200)
#        self.assertEqual(no_response.status_code, 404)
#        self.assertContains(response, 'A good title')
#        self.assertTemplateUsed(response, 'book_detail.html')
#
#    def test_book_create_view(self): # new
#        response = self.client.book(reverse('book_new'), {
#            'title': 'New title',
#            'body': 'New text',
#            'author': self.user.id,
#        })
#        self.assertEqual(response.status_code, 302)
#        self.assertEqual(Post.objects.last().title, 'New title')
#        self.assertEqual(Post.objects.last().body, 'New text')
#
#    def test_book_update_view(self): # new
#        response = self.client.book(reverse('book_edit', args='1'), {
#            'title': 'Updated title',
#            'body': 'Updated text',
#        })
#        self.assertEqual(response.status_code, 302)
#
#    def test_book_delete_view(self): # new
#        response = self.client.book(
#            reverse('book_delete', args='1'))
#        self.assertEqual(response.status_code, 302)
