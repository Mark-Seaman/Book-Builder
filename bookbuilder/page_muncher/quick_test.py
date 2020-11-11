from requests import get
# from book.models import Book


def test_quick():
    # test_book_list()
    # test_book_list()
    test_pytest()


def test_pytest():
    assert True
    assert 1 == 1


def test_book_view():
    response = get('http://127.0.0.1:8002/book/')
    assert response.status_code == 200
    text = response.content.decode('utf-8')
    assert '<a href="/">Book Builder</a>' in text
    print(text)


# def test_book_list():
#     for book in Book.objects.all():
#         print(book.author.name, ' -- ', book.title)


def test_shrinking_world():
    response = get('http://shrinking-world.com/course/cs350')
    assert response.status_code == 200
    text = response.content.decode('utf-8')
    assert '<a href="https://shrinking-world.com" class="navbar-brand">Shrinking World</a>' in text
    print(text)
