from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from markdown import markdown
    


from .author import add_author, delete_author, get_author, list_authors
from .book import add_book, delete_book, get_book, list_books
from .chapter import add_chapter, delete_chapter, get_chapter, get_chapter_num, list_chapters, set_chapter_title
from .models import Author, Book


def create_test_user():
    return get_user_model().objects.create_user(username='TEST_DUDE', email='me@here.com', password='secret')


# -----------------------------------------------------
#   M a r k d o w n
#

class MarkdownTests(SimpleTestCase):
    
    def test_markdown(self):
        actual = markdown('# Headline\n\nParagraph 1\n\nParagraph 2')
        expected = '<h1>Headline</h1>\n<p>Paragraph 1</p>\n<p>Paragraph 2</p>'
        self.assertEqual(actual, expected)
        

# -----------------------------------------------------
#   A u t h o r
#

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


# -----------------------------------------------------
#   B o o k
#

class BookTests(TestCase):

    def check_book_author(self, pk, name):
        b = Book.objects.get(pk=pk)
        self.assertEqual(b.author.name, name)

    def check_book_title(self, pk, title):
        b = Book.objects.get(pk=pk)
        self.assertEqual(b.title, title)

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

    def test_delete_book(self):
        delete_book('Tale of Two Cities')
        self.check_num_books(0)


# -----------------------------------------------------
#   C h a p t e r
#

class ChapterTests(TestCase):
    
    def check_num_chapters(self, book, num):
        self.assertEqual(len(list_chapters(book)), num)

    def check_title(self, num, title):
        self.assertEqual(get_chapter_num(self.book, num).title, title)

    def check_order(self, num, title):
        self.assertEqual(get_chapter(self.book, title).chapter_num, num)

    def setUp(self):
        self.user = create_test_user()
        author = add_author(self.user, 'Charles Dickens')
        self.book = add_book('Tale of Two Cities', author)

    def test_chapter_model(self):
        self.check_num_chapters(self.book, 0)

    def test_create(self):
        title = 'Chapter 1 - Best of Times'
        add_chapter(self.book, title)
        self.check_order(1, title)
        self.check_title(1, title)
        title = 'Chapter 2 - Worst of Times'
        add_chapter(self.book, title)
        self.check_order(2, title)
        self.check_title(2, title)
        self.check_num_chapters(self.book, 2)

    def test_update(self):
        title = 'Chapter 1 - Best of Times'
        add_chapter(self.book, title)
        self.check_title(1, title)
        title = 'Chapter 2 - Worst of Times'
        set_chapter_title(self.book, 1, title)
        self.check_title(1, title)

    def test_delete(self):
        add_chapter(self.book, 'Chapter 1 - Best of Times')
        add_chapter(self.book, 'Chapter 2 - Worst of Times')
        delete_chapter(self.book, 1)
        self.check_title(2, 'Chapter 2 - Worst of Times')
        self.check_num_chapters(self.book, 1)


