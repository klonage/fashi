from django.db import models

# Create your models here.


class Shop(models.Model):
    name = models.CharField(max_length=20)
    shop_url = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' (' + self.shop_url + ')'


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

    def __str__(self):
        return self.name


class Compositor(models.Model):
    percentage_value = models.IntegerField()
    name = models.ForeignKey(CompositorType)

    def __str__(self):
        return str(self.name) + ': ' + str(self.percentage_value) + '%'


class Size(models.Model):
    TYPES = [(0, 'uni'), (1, 'pl-number')]
    number_value = models.IntegerField()
    uni_value = models.IntegerField(choices=UniSizes.CHOICES, blank=True, null=True)
    size_type = models.IntegerField(choices=TYPES, blank=True, null=True)

    def __str__(self):
        return str(self.get_size()) + ' (' + str(self.TYPES[self.size_type][1]) + ')'

    def get_size(self):
        return self.number_value if self.size_type == 1 else self.uni_value


class Gender(models.Model):
    MALE = 0
    FEMALE = 1
    CHOICES = [(MALE, 'Male'), (FEMALE, 'Female')]


class Price(models.Model):
    currency = models.CharField(max_length=3)
    value = models.FloatField()

    def __str__(self):
        return str(self.value) + self.currency


class ClothesType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Clothes(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.OneToOneField(Price)
    gender = models.IntegerField(choices=Gender.CHOICES)
    picture_url = models.CharField(max_length=200, default='')
    item_url = models.CharField(max_length=200, default='')
    shop = models.ForeignKey(Shop)
    compositors = models.ManyToManyField(Compositor)
    available_sizes = models.ManyToManyField(Size)
    clothes_type = models.ForeignKey(ClothesType)
    colors = models.TextField() #todo !!!
