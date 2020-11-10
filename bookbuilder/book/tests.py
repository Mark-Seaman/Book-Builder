from django.contrib.auth import get_user_model
from django.test import Client, SimpleTestCase
from markdown import markdown


def create_test_user():
    return get_user_model().objects.create_user(username='TEST_DUDE', email='me@here.com', password='secret')


# -----------------------------------------------------
#   M a r k d o w n

class MarkdownTests(SimpleTestCase):
    
    def test_markdown(self):
        actual = markdown('# Headline\n\nParagraph 1\n\nParagraph 2')
        expected = '<h1>Headline</h1>\n<p>Paragraph 1</p>\n<p>Paragraph 2</p>'
        self.assertEqual(actual, expected)


# -----------------------------------------------------
#   C l i e n t

def test_client():
    response = Client().get('/book/1')
    assert response.status_code == 200
    print(response.content)


# -----------------------------------------------------
#   V i e w s

class ViewsTests(SimpleTestCase):

    def test_page_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, template_name='home.html')
        self.assertTemplateUsed(response, template_name='book_theme.html')
        self.assertTemplateUsed(response, template_name='_header.html')
        self.assertTemplateUsed(response, template_name='_footer.html')
        self.assertTemplateUsed(response, template_name='_user.html')

    def test_title(self):
        response = self.client.get('/')
        self.assertContains(response, '<title>Book Builder</title>')

    def test_style(self):
        response = self.client.get('/')
        self.assertContains(response, '<link rel="shortcut icon" type="image/png" href="/static/Bear.favicon.ico"/>')
        self.assertContains(response, '<link rel="stylesheet" href="/static/shrinking-world.css">')

    def test_get_started(self):
        response = self.client.get('/')
        self.assertContains(response, '<a href="/book/" class="btn btn-success">Get Started</a>')

    def test_missing_page(self):
        response = self.client.get('xxx')
        self.assertEqual(response.status_code, 404)
