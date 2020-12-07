import pytest
from django.urls import reverse, resolve
from django.test import SimpleTestCase
from django.contrib.auth.models import User
from myusers import views
from myusers.models import Profile, UserRegDemographics
from surveys.views import surveys, environmental_detail


class TestUrls(SimpleTestCase):

    def test_register_url(self):
        path = reverse('register')
        assert resolve(path).view_name == 'register'

    def test_surveys_url(self):
        path = reverse('surveys')
        assert resolve(path).view_name == 'surveys'

    def test_logins_url(self):
        path = reverse('login')
        assert resolve(path).view_name == 'login'
