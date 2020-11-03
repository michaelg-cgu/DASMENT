from django.urls import reverse, resolve


class TestUrls:

    def test_detail_url(self):
        path = reverse('register')
        assert resolve(path).view_name == 'register'


    #def test_surveys_url(self):
    #    path = reverse('surveys')
    #    assert resolve(path).view_name == 'surveys'

    #Simple unit tests of urls of admin page, food, environmental allergy, etc
