import pytest
from django.urls import reverse, resolve
from django.test import SimpleTestCase
from surveys.views import surveys, environmental_detail
from myusers import views
from myusers.models import Profile, UserRegDemographics


#class TestUrls(SimpleTestCase):

#    def test_register_url(self):
#        url = reverse('register')
#        print(resolve(url))
#        self.assertEquals(resolve(url).view_name, user_views)

#    def test_profile_url(self):
#        url = reverse('profile')
#        print(resolve(url))
#        self.assertEquals(resolve(url).view_name, user_views)

#    def test_surveys_url(self):
#        url = reverse('surveys')
#        print(resolve(url))
#        self.assertEquals(resolve(url).view_name, surveys)

#    def test_environmental_survey_url(self):
#        url = reverse('surveys/environmental')
#        print(resolve(url))
#        self.assertEquals(resolve(url).view_name, environmental_detail)


#    def test_detail_url(self):
#        path = reverse('register')
#        assert resolve(path).view_name == 'register'
#
#    def test_surveys_url(self):
#        path = reverse('surveys')
#        assert resolve(path).view_name == 'surveys'
