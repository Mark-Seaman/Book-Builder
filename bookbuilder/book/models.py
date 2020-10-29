'''

Data Model Classes

* Reader
    * user*
* Author
    * user*
    * name
* Book
    * author*
    * title
* Chapter
    * book*
    * title
    * chapter_num
'''


from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.pk} - {self.name}'


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)

    def __str__(self):
        return f'{self.pk} - {self.title} by {self.author.name}'

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])


class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, editable=False)
    title = models.CharField(max_length=100)
    chapter_num = models.IntegerField()
    text = models.TextField(default='No Chapter Text')

    def __str__(self):
        return f'Chapter {self.chapter_num} - {self.title}'

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.book.id)])

