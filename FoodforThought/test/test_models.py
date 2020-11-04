#import se
#import re
#import pytest

#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

#HOMEPAGE = 'http://localhost:8000'

#USER_NAME = 'testuser'
#USER_PASSWORD = 'query123'

#def test_homepage(driver):
#    driver.get(HOMEPAGE)
#    expected = "FoodforThought"
#    assert driver.title == expected

#def test_loginandlogout(driver):
#    driver.get(HOMEPAGE)
#    driver.find_element_by_id('loginlink').click()
#    driver.find_element_by_name('username').send_keys(USER_NAME)
#    driver.find_element_by_id('logoutlink').click()
#    expected = "You have logged out."
#    p = driver.find_element_by_tag_name('p')
#    assert p.text == expected

#def test_foodallergies(driver):
#    driver.get(HOMEPAGE)
    #driver.find_element_by_id('').click()
    #expected = ""
    #h2 = driver.find_element_by_tag_name('h2')
    #assert h2.text == expected

#def test_environmentallergies(driver):
#    driver.get(HOMEPAGE)
