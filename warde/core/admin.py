from django.contrib import admin
from core.models import ItemType
from core.models import Gender
from core.models import Style
from core.models import Picture
from core.models import ClothesItem
from core.models import UserInfo
from core.models import UserStyleTemp
# Register your models here.

admin.site.register(ItemType)
admin.site.register(Gender)
admin.site.register(Style)
admin.site.register(Picture)
admin.site.register(ClothesItem)
admin.site.register(UserInfo)
admin.site.register(UserStyleTemp)
