from django.contrib.auth.models import User
import os
import django
from django.conf import settings
import pytest

pytestmark = pytest.mark.django_db


def test_registration_register():

    user = User.objects.create_user('test_register', 'test_register@example.com', 'password')
    user.save()
    retrieved_user = User.objects.get(email='test_register@example.com')
    if retrieved_user is not None:
        assert True
    else:
        assert False
