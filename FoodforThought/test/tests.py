import pytest
from django.urls import reverse, resolve
from django.test import SimpleTestCase
from surveys.views import surveys, environmental_detail
from myusers import views
from myusers.models import Profile, UserRegDemographics


@pytest.mark.django_db
def test_user_iscreated():
    User.objects.create_user('Michael', 'MichaelPassword')
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_user_profile_isCreated():
    user_info = UserRegDemographics.objects.create(gender_choices='Male')
    assert user_info.gender_choices == 'Male'

@pytest.mark.django_db
def test_view_registration_page(client):
   url = reverse('register')
   #print(resolve(url))
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test__view_profile_page(self):
    url = reverse('profile')
    #print(resolve(url))
    response = client.get(url)
    assert response.status_code == 200
