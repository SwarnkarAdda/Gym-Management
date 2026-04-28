from django.db import models

# Create your models here.

class Member(models.Model):

    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=100)
    joiningDate = models.CharField(max_length=20)
    expireingDate = models.CharField(max_length=20)
    workoutTime = models.CharField(max_length=25)
    plan = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Trainer(models.Model):

    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=100)
    experience = models.IntegerField()
    specialty = models.CharField(max_length=100)
    joiningDate = models.CharField(max_length=20)
    salary = models.IntegerField()
    shift = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Admin(models.Model):

    email = models.CharField(max_length=50)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.email