from django.contrib import admin
from django.urls import path

from .views import BookAdd, BookDetail, BookEdit, BookList, ChapterAdd, ChapterDetail, ChapterEdit, ChapterList, \
    PageView

urlpatterns = [

    # Admin
    path(r'admin/', admin.site.urls),

    # Page Prototype
    path('', PageView.as_view()),
    path('<str:template>', PageView.as_view()),

    # Book
    path('book/',               BookList.as_view(),     name='book_list'),
    path('book/<int:pk>',       BookDetail.as_view(),   name='book_detail'),
    path('book/add',            BookAdd.as_view(),      name='book_add'),
    path('book/<int:pk>/',      BookEdit.as_view(),     name='book_edit'),

    # Chapter
    path('chapter/',            ChapterList.as_view(),   name='chapter_list'),
    path('chapter/<int:pk>',    ChapterDetail.as_view(), name='chapter_detail'),
    path('chapter/<int:book_id>/add', ChapterAdd.as_view(),    name='chapter_add'),
    path('chapter/<int:pk>/',   ChapterEdit.as_view(),   name='chapter_edit'),

]
