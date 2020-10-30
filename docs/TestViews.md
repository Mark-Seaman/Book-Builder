# How to Test Views

Using the Django Test framework

## SimpleTestCase

### Data or No Data?
* If data operations are needed then use TestCase as the base class
* If no data operations are needed then use SimpleTestCase as the base class


```python
from django.test import SimpleTestCase, TestCase

# No data
class ViewsTests(SimpleTestCase)

# Book data
class BookViewsTests(TestCase)    
                            
```


### Check for Page
* Use requests to fetch the page from a URL
* Check the status code (200 is success)
* Test multiple pages


```python
from django.test import SimpleTestCase

class ViewsTests(SimpleTestCase):

    def test_page_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
```


### Check Missing Page
* Use requests to fetch the page from a URL
* Check the status code (404 is page not found)


```python
from django.test import SimpleTestCase

class ViewsTests(SimpleTestCase):

    def test_missing_page(self):
        response = self.client.get('xxx')
        self.assertEqual(response.status_code, 404)
                            
```


### Check for Templates Used
* Composite views use many templates
* Look for all the templates that are used


```python
from django.test import SimpleTestCase

class ViewsTests(SimpleTestCase):

    def test_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, template_name='home.html')
        self.assertTemplateUsed(response, template_name='book_theme.html')
        self.assertTemplateUsed(response, template_name='_header.html')
        self.assertTemplateUsed(response, template_name='_footer.html')
        self.assertTemplateUsed(response, template_name='_user.html')                        
```


### Check for HTML Fragments
* Use "assertContains" to match known fragments
    * title
    * stylesheet
    * favicon
    * key links
    * headline


```python
from django.test import SimpleTestCase

class ViewsTests(SimpleTestCase):

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
```

