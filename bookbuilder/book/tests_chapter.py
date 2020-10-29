from django.test import TestCase

from book.author import add_author
from book.book import add_book
from book.chapter import add_chapter, delete_chapter, get_chapter, get_chapter_num, list_chapters, set_chapter_title
from book.tests import create_test_user


# -----------------------------------------------------
#   C h a p t e r

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