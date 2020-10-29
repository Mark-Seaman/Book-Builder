from django.test import TestCase

from book.author import add_author, delete_author, get_author, list_authors
from book.models import Author
from book.tests import create_test_user


# -----------------------------------------------------
#   A u t h o r

class AuthorTests(TestCase):

    def check_author_name(self, pk, name):
        a = Author.objects.get(pk=pk)
        self.assertEqual(a.name, name)

    def check_author_user(self, pk, username):
        a = Author.objects.get(pk=pk)
        self.assertEqual(a.user.username, username)

    def check_num_authors(self, num):
        self.assertEqual(len(list_authors()), num)

    def setUp(self):
        self.user = create_test_user()
        self.author = add_author(self.user, 'Charles Dickens')

    def test_author_model(self):
        self.check_num_authors(1)
        self.check_author_name(1, 'Charles Dickens')
        self.check_author_user(1, 'TEST_DUDE')

    def test_create_author(self):
        self.check_num_authors(1)
        add_author(self.user, 'Jack London')
        self.check_author_name(2, 'Jack London')
        self.check_author_user(2, 'TEST_DUDE')
        self.check_num_authors(2)

    def test_list_authors(self):
        self.check_num_authors(1)
        self.assertEqual(get_author('Charles Dickens').pk, 1)

    def test_update_author(self):
        self.check_num_authors(1)
        a = get_author('Charles Dickens')
        a.name = 'George Orwell'
        a.save()
        self.check_author_name(1, 'George Orwell')

    def test_delete_author(self):
        delete_author('Charles Dickens')
        self.check_num_authors(0)