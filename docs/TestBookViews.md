### Test Book Views
* Test the views for the Book data model
* Views
    * book_list
    * book_add
    * book_edit
    * book_detail
    * book_delete
    

```python
# test_book.py

class BookViewsTests(TestCase):

    def setUp(self):
        self.user = create_test_user()
        self.author = add_author(self.user, 'Charles Dickens')
        self.book = add_book('Tale of Two Cities', self.author)
        response = self.client.login(username='TEST_DUDE', password='secret')
        self.assertEqual(response, True)

    def test_get_absolute_url(self):
        self.assertEqual(self.book.get_absolute_url(), '/book/1')

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Tale of Two Cities')
        self.assertContains(response, '<li>', count=1)
        self.assertTemplateUsed(response, 'book_list.html')

    def test_book_detail_view(self):
        response = self.client.get('/book/1')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Charles Dickens')
        self.assertContains(response, 'Tale of Two Cities')
        self.assertContains(response, 'No description')
        self.assertTemplateUsed(response, 'book_detail.html')
        no_response = self.client.get('/book/100000')
        self.assertEqual(no_response.status_code, 404)

    def test_book_create_view(self):
        new_book = dict(title="Sea Wolf", description='No big deal')
        response = self.client.post(reverse('book_add'), new_book)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(Book.objects.all()), 2)
        book = Book.objects.last()
        self.assertEqual(book.author.name, 'Charles Dickens')
        self.assertEqual(book.title, 'Sea Wolf')
        self.assertEqual(book.description, 'No big deal')

    def test_book_update_view(self):
        kwargs = dict(title='Lord of the Rings', description='Great story')
        response = self.client.post(reverse('book_edit', args='1'), kwargs)
        self.assertEqual(response.status_code, 302)
        b = Book.objects.get(pk=1)
        self.assertEqual(b.title, 'Lord of the Rings')

    # def test_book_delete_view(self):
    #     response = self.client.post(reverse('book_delete', args='1'))
    #     self.assertEqual(response.status_code, 302)
```