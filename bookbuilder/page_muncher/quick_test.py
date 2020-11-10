from requests import get


def test_quick():
    test_pytest()


def test_pytest():
    assert True
    assert 1 == 1


def test_request():
    response = get('https://shrinking-world.com')
    assert response.status_code == 200
    text = response.content.decode('utf-8')
    assert '<a href="">Shrinking World Training</a>' in text
    print(text)
