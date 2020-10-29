from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import datetime

# Create your models here.
# extend the user model to have one-to-one relationship

# can add what ever i want to this model, depending on DRY


class Profile(models.Model):
    """building user upload photo model. CASCADE = delete user,
    and therefore delete profile."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # print out the user name and profile
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kawargs):
        super(Profile, self).save()  # run the save method of the parent

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class UserRegDemographics(models.Model):
    male = 'male'
    female = 'female'
    other = 'other'
    gender_choices = [(male, 'Male'), (female, 'Female'), (other, 'Other')]
    location = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=gender_choices, default=other)
    birthdate = models.DateField(default=datetime.date.today)
    my_weight = models.PositiveIntegerField(default=150)
    my_referral = models.CharField(max_length=100, default='The Internet')

    def __str__(self):
        return 'filler text'
# should this be a child class of the above?
