from django.contrib.auth.models import User
from myusers.models import UserRegDemographics, Profile
import os
import django
from django.conf import settings
import pytest

pytestmark = pytest.mark.django_db


def test_registration_isValid():
    user = User.objects.create_user('test_register', 'test_register@example.com', 'password')
    user.save()
    retrieved_user = User.objects.get(email='test_register@example.com')
    if retrieved_user is not None:
        assert True
    else:
        assert False

def test_registration_username():
    user = User.objects.create_user('test_register', 'test_register@example.com', 'password')
    user.save()
    retrieved_user = User.objects.get(email='test_register@example.com')
    assert user.get_username() == 'test_register'

@pytest.mark.xfail
def test_registration_wrong_username():
    user = User.objects.create_user('test_register', 'test_register@example.com', 'password')

    assert user.get_username() == 'Wrongusername'

def test_registration_email():
    user = User.objects.create_user('test_register', 'test_register@example.com', 'password')
    assert user.email == 'test_register@example.com'

@pytest.mark.xfail
def test_registration_wrong_email():
    user = User.objects.create_user('test_register', 'test_register@example.com', 'password')

    assert user.email == 'wrong@example.com'

def test_registration_password():
    user = User.objects.create_user('test_register', 'test_register@example.com', 'password')
    user.set_password('password')

    assert user.check_password('password') == True

@pytest.mark.xfail
def test_registration_wrong_password():
    user = User.objects.create_user('test_register', 'test_register@example.com', 'password')
    user.set_password('password')

    assert user.check_password('klfjaskldf') == True

#@pytest.mark.django_db
#def test_Profile_User():
#    user_zero = User.objects.create_user('test_register', 'test_register@example.com', 'password')
#    profile = Profile.objects.create(user=user_zero, image= 'default.jpg')
#    assert profile.user == user_zero

#@pytest.mark.django_db
#def test_Profile_Image():
#    user_zero = User.objects.create_user('test_register', 'test_register@example.com', 'password')
#    user_zero.save()
#    profile = Profile.objects.create(user=user_zero, image= 'default.jpg')
#    assert user_zero.profile.image == 'default.jpg'
