import pytest
from selenium import webdriver


# С помощью этой функции мы считываем значение из коммандной строки (--browser)
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    # Достаем значение из коммандной строчки
    browser_name = request.config.getoption("browser_name")
    browser = None

    # Таким образом мы определеяем, какой браузер будем использовать для тестов
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

# ВАЖНО. pytest инициализирует такие файлы в каждой директории. Лучше не создавать файл в корневой директории и в
# подкаталогах. Либо один на весь проект в корне, либо по одному в каждой поддиректории
