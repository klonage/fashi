from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ItemType(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50, unique=True)


class Gender(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=20, unique=True)


class Style(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=30, unique=True)


class Picture(models.Model):
    def __str__(self):
        return self.address

    address = models.URLField(unique=True)


class ClothesItem(models.Model):
    color = models.IntegerField()
    type = models.ForeignKey(ItemType)
    gender = models.ForeignKey(Gender)
    style = models.ForeignKey(Style)
    description = models.TextField()
    images = models.ManyToManyField(Picture, blank=True)
    itemname = models.CharField(max_length=30, blank=True)
    address = models.URLField()
    price = models.FloatField()
    display = models.BooleanField(default=True)


class UserInfo(models.Model):
    def __str__(self):
        return "Info for: " + self.user.username

    user = models.OneToOneField(User)
    bought_clothes = models.ManyToManyField(ClothesItem, blank=True)
    gender = models.ForeignKey(Gender)


class UserStyleTemp(models.Model):
    def __str__(self):
        return str(self.value) + " of user " + self.userinfo.user.username + " of style " + self.style.name

    style = models.ForeignKey(Style, blank=True)
    value = models.FloatField()
    userinfo = models.ForeignKey(UserInfo)

