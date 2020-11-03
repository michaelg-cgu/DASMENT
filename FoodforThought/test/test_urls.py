from django.test import SimpleTestCase
from django.urls import reverse, resolve
from surveys.views import surveys, environmental_detail
from myusers import views


class TestUrls(SimpleTestCase):

    def test_register_url(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).view_name, user_views)

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
