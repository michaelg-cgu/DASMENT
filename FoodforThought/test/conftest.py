import os
import re
import django
from django.conf import settings
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FoodforThought.settings')

#def pytest_configure():
#    settings.DEBUG = False
#    django.setup()

#DEFAULT_ENGINE = 'django.db.backends.sqlite3'

#@pytest.fixture(scope="module")
#def driver():
#    driver = webdriver.Chrome()
#    yield driver
#    driver.quit()


#HOMEPAGE = 'http://127.0.0.1:8000/'

#USER_NAME = 'testuser'
#USER_PASSWORD = 'password'


#def test_homepage(driver):
#    driver.get(HOMEPAGE)
#    exp = 'Django Blog'
#    assert driver.title == HOMEPAGE
