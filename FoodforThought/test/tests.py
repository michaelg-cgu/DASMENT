import pytest
import datetime
from django.utils import timezone
from django.urls import reverse, resolve
from django.test import SimpleTestCase
from django.db import models
from surveys.views import surveys, environmental_detail
from myusers import views
from myusers.models import Profile, UserRegDemographics
from surveys.models import FoodAllergy, Environmental
from blog.models import Post
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_iscreated():
    User.objects.create_user('Michael', 'MichaelPassword')
    assert User.objects.count() == 1

#Additional Demographic Information Testing for Registration Page
@pytest.mark.django_db
def test_user_demographics_location():
    user_one = User.objects.create_user('Michael', 'michael@michael.com', 'password')
    user_demo = UserRegDemographics.objects.create(user= user_one, location='Claremont', age=50, gender='Male',
    birthdate='2020-07-12', my_weight=150, my_referral='The Internet')
    user_demo.save()
    assert user_demo.location == 'Claremont'

@pytest.mark.django_db
@pytest.mark.xfail
def test_user_demographics_badlocation():
    user_one = User.objects.create_user('Michael', 'michael@michael.com', 'password')
    user_demo = UserRegDemographics.objects.create(user= user_one, location='Claremont', age=50, gender='Male',
    birthdate='2020-07-12', my_weight=150, my_referral='The Internet')
    user_demo.save()
    assert user_demo.location == 'Los Angeles'

@pytest.mark.django_db
def test_user_demographics_age():
    user_one = User.objects.create_user('Michael', 'michael@michael.com', 'password')
    user_demo = UserRegDemographics.objects.create(user= user_one, location='Claremont', age=50, gender='Male',
    birthdate='2020-07-12', my_weight=150, my_referral='The Internet')
    user_demo.save()
    assert user_demo.age == 50

@pytest.mark.django_db
def test_user_demographics_gender():
    user_one = User.objects.create_user('Michael', 'michael@michael.com', 'password')
    user_demo = UserRegDemographics.objects.create(user= user_one, location='Claremont', age=50, gender='Male',
    birthdate='2020-07-12', my_weight=150, my_referral='The Internet')
    user_demo.save()
    assert user_demo.gender == 'Male'

@pytest.mark.django_db
def test_user_demographics_birthdate():
    user_one = User.objects.create_user('Michael', 'michael@michael.com', 'password')
    user_demo = UserRegDemographics.objects.create(user= user_one, location='Claremont', age=50, gender='Male',
    birthdate='2020-07-12', my_weight=150, my_referral='The Internet')
    user_demo.save()
    assert user_demo.birthdate == '2020-07-12'

@pytest.mark.django_db
def test_user_demographics_weight():
    user_one = User.objects.create_user('Michael', 'michael@michael.com', 'password')
    user_demo = UserRegDemographics.objects.create(user= user_one, location='Claremont', age=50, gender='Male',
    birthdate='2020-07-12', my_weight=150, my_referral='The Internet')
    user_demo.save()
    assert user_demo.my_weight == 150

@pytest.mark.django_db
@pytest.mark.xfail()
def test_user_demographics_wrongweight():
    user_one = User.objects.create_user('Michael', 'michael@michael.com', 'password')
    user_demo = UserRegDemographics.objects.create(user= user_one, location='Claremont', age=50, gender='Male',
    birthdate='2020-07-12', my_weight=150, my_referral='The Internet')
    user_demo.save()
    assert user_demo.my_weight == 200

@pytest.mark.django_db
def test_user_demographics_referral():
    user_one = User.objects.create_user('Michael', 'michael@michael.com', 'password')
    user_demo = UserRegDemographics.objects.create(user= user_one, location='Claremont', age=50, gender='Male',
    birthdate='2020-07-12', my_weight=150, my_referral='The Internet')
    user_demo.save()
    assert user_demo.my_referral == 'The Internet'














#Testing for Food Allergy Form components
@pytest.mark.django_db
def test_foodallergy_none():
    user_one = User.objects.create_user('Michael', 'Michael@michael.com', 'password')
    allergy=FoodAllergy.objects.create(user= user_one, allergy1='None', allergy2='None', allergy3='None',
    allergy4='None', allergy5='None')
    assert allergy.allergy1=='None'

@pytest.mark.django_db
def test_foodallergy_dairy():
    user_one = User.objects.create_user('Michael', 'Michael@michael.com', 'password')
    allergy=FoodAllergy.objects.create(user= user_one, allergy1='Dairy', allergy2='None', allergy3='None',
    allergy4='None', allergy5='None')
    assert allergy.allergy1=='Dairy'

@pytest.mark.django_db
def test_foodallergy_soy():
    user_one = User.objects.create_user('Michael', 'Michael@michael.com', 'password')
    allergy=FoodAllergy.objects.create(user= user_one, allergy1='Soy', allergy2='None', allergy3='None',
    allergy4='None', allergy5='None')
    assert allergy.allergy1=='Soy'

@pytest.mark.django_db
def test_foodallergy_wheat():
    user_one = User.objects.create_user('Michael', 'Michael@michael.com', 'password')
    allergy=FoodAllergy.objects.create(user= user_one, allergy1='Wheat', allergy2='None', allergy3='None',
    allergy4='None', allergy5='None')
    assert allergy.allergy1=='Wheat'

@pytest.mark.django_db
def test_foodallergy_shellfish():
    user_one = User.objects.create_user('Michael', 'Michael@michael.com', 'password')
    allergy=FoodAllergy.objects.create(user= user_one, allergy1='Shellfish', allergy2='None', allergy3='None',
    allergy4='None', allergy5='None')
    assert allergy.allergy1=='Shellfish'

@pytest.mark.django_db
def test_foodallergy_nuts():
    user_one = User.objects.create_user('Michael', 'Michael@michael.com', 'password')
    allergy=FoodAllergy.objects.create(user= user_one, allergy1='Nuts', allergy2='None', allergy3='None',
    allergy4='None', allergy5='None')
    assert allergy.allergy1=='Nuts'

@pytest.mark.django_db
@pytest.mark.xfail
def test_foodallergy_baddata():
    user_one = User.objects.create_user('Michael', 'Michael@michael.com', 'password')
    allergy=FoodAllergy.objects.create(user= user_one, allergy1='None', allergy2='None', allergy3='None',
    allergy4='None', allergy5='None')
    assert allergy.allergy1=='Nuts'

@pytest.mark.django_db
@pytest.mark.xfail
def test_foodallergy_baddataagain():
    user_one = User.objects.create_user('Michael', 'Michael@michael.com', 'password')
    allergy=FoodAllergy.objects.create(user= user_one, allergy1='None', allergy2='None', allergy3='None',
    allergy4='None', allergy5='None')
    assert allergy.allergy2=='Nuts'








#Testing Environmental Allergy Form allergy components
@pytest.mark.django_db
def test_envallergy_allergyone():
    user_one = User.objects.create_user('Michael', 'Michael@michael.com', 'password')
    environment=Environmental.objects.create(user= user_one, eallergy1='None', severity1='None',
    eallergy2='None', severity2='None',
    eallergy3='None', severity3='None',
    eallergy4='None', severity4='None',
    eallergy5='None', severity5='None')

    assert environment.eallergy1=='None'

@pytest.mark.django_db
def test_envallergy_allergytwo():
    user_one = User.objects.create_user('Michael', 'Michael@michael.com', 'password')
    environment=Environmental.objects.create(user= user_one, eallergy1='None', severity1='None',
    eallergy2='Grass', severity2='None',
    eallergy3='None', severity3='None',
    eallergy4='None', severity4='None',
    eallergy5='None', severity5='None')

    assert environment.eallergy2=='Grass'

@pytest.mark.django_db
def test_envallergy_allergythree():
    user_one = User.objects.create_user('Michael', 'Michael@michael.com', 'password')
    environment=Environmental.objects.create(user= user_one, eallergy1='None', severity1='None',
    eallergy2='Grass', severity2='None',
    eallergy3='Dust', severity3='None',
    eallergy4='None', severity4='None',
    eallergy5='None', severity5='None')

    assert environment.eallergy3=='Dust'

@pytest.mark.django_db
def test_envallergy_allergyfour():
    user_one = User.objects.create_user('Michael', 'Michael@michael.com', 'password')
    environment=Environmental.objects.create(user= user_one, eallergy1='None', severity1='None',
    eallergy2='Grass', severity2='None',
    eallergy3='None', severity3='None',
    eallergy4='Pollen', severity4='None',
    eallergy5='None', severity5='None')

    assert environment.eallergy4=='Pollen'

@pytest.mark.django_db
def test_envallergy_allergyfive():
    user_one = User.objects.create_user('Michael', 'Michael@michael.com', 'password')
    environment=Environmental.objects.create(user= user_one, eallergy1='None', severity1='None',
    eallergy2='Grass', severity2='None',
    eallergy3='None', severity3='None',
    eallergy4='Pollen', severity4='None',
    eallergy5='Pet Dander', severity5='None')

    assert environment.eallergy5=='Pet Dander'

@pytest.mark.django_db
def test_envallergy_allergysix():
    user_one = User.objects.create_user('Michael', 'Michael@michael.com', 'password')
    environment=Environmental.objects.create(user= user_one, eallergy1='None', severity1='None',
    eallergy2='Grass', severity2='None',
    eallergy3='None', severity3='None',
    eallergy4='Pollen', severity4='None',
    eallergy5='Mold', severity5='None')

    assert environment.eallergy5=='Mold'

@pytest.mark.django_db
def test_envallergy_allergylast():
    user_one = User.objects.create_user('Michael', 'Michael@michael.com', 'password')
    environment=Environmental.objects.create(user= user_one, eallergy1='None', severity1='None',
    eallergy2='Insect Bites', severity2='None',
    eallergy3='None', severity3='None',
    eallergy4='Pollen', severity4='None',
    eallergy5='None', severity5='None')

    assert environment.eallergy2=='Insect Bites'

@pytest.mark.django_db
@pytest.mark.xfail
def test_envallergy_badallergydata():
    user_one = User.objects.create_user('Michael', 'Michael@michael.com', 'password')
    environment=Environmental.objects.create(user= user_one, eallergy1='None', severity1='Mild',
    eallergy2='Insect Bites', severity2='Moderate',
    eallergy3='None', severity3='Severe',
    eallergy4='Pollen', severity4='Toxic',
    eallergy5='None', severity5='None')

    assert environment.eallergy1=='Toxic'




#Testing Environmental Allergy Form severity components
@pytest.mark.django_db
def test_envallergy_severityNone():
    user_one = User.objects.create_user('Michael', 'Michael@michael.com', 'password')
    environment=Environmental.objects.create(user= user_one, eallergy1='None', severity1='None',
    eallergy2='Insect Bites', severity2='None',
    eallergy3='None', severity3='None',
    eallergy4='Pollen', severity4='None',
    eallergy5='None', severity5='None')

    assert environment.severity1=='None'

@pytest.mark.django_db
def test_envallergy_severityMild():
    user_one = User.objects.create_user('Michael', 'Michael@michael.com', 'password')
    environment=Environmental.objects.create(user= user_one, eallergy1='None', severity1='Mild',
    eallergy2='Insect Bites', severity2='None',
    eallergy3='None', severity3='None',
    eallergy4='Pollen', severity4='None',
    eallergy5='None', severity5='None')

    assert environment.severity1=='Mild'

@pytest.mark.django_db
def test_envallergy_severityModerate():
    user_one = User.objects.create_user('Michael', 'Michael@michael.com', 'password')
    environment=Environmental.objects.create(user= user_one, eallergy1='None', severity1='Mild',
    eallergy2='Insect Bites', severity2='Moderate',
    eallergy3='None', severity3='None',
    eallergy4='Pollen', severity4='None',
    eallergy5='None', severity5='None')

    assert environment.severity2=='Moderate'

@pytest.mark.django_db
def test_envallergy_severitySevere():
    user_one = User.objects.create_user('Michael', 'Michael@michael.com', 'password')
    environment=Environmental.objects.create(user= user_one, eallergy1='None', severity1='Mild',
    eallergy2='Insect Bites', severity2='Moderate',
    eallergy3='None', severity3='Severe',
    eallergy4='Pollen', severity4='None',
    eallergy5='None', severity5='None')

    assert environment.severity3=='Severe'

@pytest.mark.django_db
def test_envallergy_severityToxic():
    user_one = User.objects.create_user('Michael', 'Michael@michael.com', 'password')
    environment=Environmental.objects.create(user= user_one, eallergy1='None', severity1='Mild',
    eallergy2='Insect Bites', severity2='Moderate',
    eallergy3='None', severity3='Severe',
    eallergy4='Pollen', severity4='Toxic',
    eallergy5='None', severity5='None')

    assert environment.severity4=='Toxic'

@pytest.mark.django_db
@pytest.mark.xfail
def test_envallergy_badseveritydata():
    user_one = User.objects.create_user('Michael', 'Michael@michael.com', 'password')
    environment=Environmental.objects.create(user= user_one, eallergy1='None', severity1='Mild',
    eallergy2='Insect Bites', severity2='Moderate',
    eallergy3='None', severity3='Severe',
    eallergy4='Pollen', severity4='Toxic',
    eallergy5='None', severity5='None')

    assert environment.severity4=='None'




#Test Blogs models.py file
@pytest.mark.django_db
def test_blog_models_title():
    user_one = User.objects.create_user('Michael', 'Michael@michael.com', 'password')
    blog = Post.objects.create(title="Allergies", content="Updates", date_posted=timezone.now(), author=user_one)
    assert blog.title=="Allergies"

@pytest.mark.django_db
def test_blog_models_content():
    user_one = User.objects.create_user('Michael', 'Michael@michael.com', 'password')
    blog = Post.objects.create(title="Allergies", content="Updates", date_posted=timezone.now(), author=user_one)
    assert blog.content=="Updates"

@pytest.mark.django_db
def test_blog_models_author():
    user_one = User.objects.create_user('Michael', 'Michael@michael.com', 'password')
    blog = Post.objects.create(title="Allergies", content="Updates", date_posted=timezone.now(), author=user_one)
    assert blog.author==user_one

@pytest.mark.django_db
@pytest.mark.xfail
def test_blog_models_baddata():
    user_one = User.objects.create_user('Michael', 'Michael@michael.com', 'password')
    blog = Post.objects.create(title="Allergies", content="Updates", date_posted=timezone.now(), author=user_one)
    assert blog.title=="Remedies"



#Additional Testing for URLS
@pytest.mark.django_db
def test_view_registration_page(client):
   url = reverse('register')
   #print(resolve(url))
   response = client.get(url)
   assert response.status_code == 200

@pytest.mark.django_db
def test_view_login_page(client):
   url = reverse('login')
   #print(resolve(url))
   response = client.get(url)
   assert response.status_code == 200
