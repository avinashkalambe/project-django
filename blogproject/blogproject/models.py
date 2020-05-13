from django.db import models

class Contact(models.Model):
    fullname = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    message = models.TextField()

