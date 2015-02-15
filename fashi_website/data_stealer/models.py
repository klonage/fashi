from django.db import models

# Create your models here.


class Shop(models.Model):
    name = models.CharField(max_length=20)
    shop_url = models.CharField(max_length=50)


class UniSizes(models.Model):
    XS = 0
    S = 1
    M = 2
    L = 3
    XL = 4
    XXL = 5
    CHOICES = [(XS, "XS"), (S, "S"), (L, "L"), (M, "M"), (L, "L"), (XL, "XL"), (XXL, "XXL")]


class CompositorType(models.Model):
    name = models.CharField(max_length=30)


class Compositor(models.Model):
    percentage_value = models.IntegerField()
    name = models.ForeignKey(CompositorType)


class Size(models.Model):
    TYPE = [(0, 'uni'), (1, 'pl-number')]
    number_value = models.IntegerField()
    uni_value = UniSizes.CHOICES

    def get_size(self):
        return self.number_value if self.TYPE == 0 else self.uni_value


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
    picture_url = models.CharField(max_length=200, default='')
    item_url = models.CharField(max_length=200, default='')
    shop = models.ForeignKey(Shop)
    compositors = models.ManyToManyField(Compositor)

