from django.db import models
from django.contrib.auth.models import User
from PIL import Image

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

    def save(self):
        super().save()  # run the save method of the parent

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
