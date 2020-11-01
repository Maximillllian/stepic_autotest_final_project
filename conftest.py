import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# С помощью этой функции мы считываем значение из коммандной строки (--browser)
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    # Достаем значение из коммандной строчки
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    browser = None

    # Таким образом мы определеяем, какой браузер будем использовать для тестов
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

# ВАЖНО. pytest инициализирует такие файлы в каждой директории. Лучше не создавать файл в корневой директории и в
# подкаталогах. Либо один на весь проект в корне, либо по одному в каждой поддиректории
