from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.firstname + ' ' + self.lastname
  
