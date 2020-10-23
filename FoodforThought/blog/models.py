from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# these are fields in the database:


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    # This is a one to many the on_delete, CASCASE, if user is deleted, post is deleted, Will want to change This
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # add other components here

    def __str__(self):
        return self.title
