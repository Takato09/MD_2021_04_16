from django.db import models


class Adduser(models.Model):

    username = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
