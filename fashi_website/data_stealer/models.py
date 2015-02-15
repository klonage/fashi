from django.db import models

# Create your models here.


class Gender(models.Model):
    MALE = 0
    FEMALE = 1
    CHOICES = [(MALE, 'Male'), (FEMALE, 'Female')]


class Price(models.Model):
    currency = models.CharField(max_length=3)
    value = models.IntegerField()


class ClothesType(models.Model):
    name = models.CharField(max_length=30)


class Clothes(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.OneToOneField(Price)
    gender = Gender.CHOICES

