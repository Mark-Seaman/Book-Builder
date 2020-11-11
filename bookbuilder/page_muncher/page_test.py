from selenium import webdriver
from requests import get


def open_browser():
    # browser = webdriver.Chrome()

    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('window-size=800x600')
    options.add_argument('headless')
    return webdriver.Chrome(options=options)


# def test_selenium():
#     browser = open_browser()
#     browser.get('http://shrinking-world.com/course/cs350')
#     browser.quit()
#
#
# def test_selenium_text():
#
#     def test_page_header(browser):
#         header_title = browser.find_element_by_css_selector('header h1')
#         header_title = header_title.get_attribute("innerHTML")
#         expected = '<a href="/course/cs350">UNC CS 350</a>'
#         assert expected in header_title
#
#     def test_links(browser):
#         links = browser.find_elements_by_css_selector('li a[href]')
#         links = [link.get_attribute("innerHTML") for link in links]
#         # print(links)
#         assert len(links) == 12
#
#     def test_html(browser):
#         assert len(browser.page_source) == 59478
#
#     def test_text(browser):
#         body_text = browser.find_element_by_tag_name('body').text
#         assert len(body_text) == 682
#
#     # Open the browser
#     browser = open_browser()
#
#     # Get the web page
#     url = 'http://shrinking-world.com/course/cs350/lesson/Index'
#     browser.get(url)
#
#     # Verify the page content
#     test_page_header(browser)
#     test_links(browser)
#     test_html(browser)
#     test_text(browser)
#
#     # Close the browser
#     browser.quit()
#
