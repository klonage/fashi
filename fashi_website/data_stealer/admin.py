from django.contrib import admin
import data_stealer.models

admin.site.register(data_stealer.models.Shop)
admin.site.register(data_stealer.models.CompositorType)
admin.site.register(data_stealer.models.Compositor)
admin.site.register(data_stealer.models.Size)
admin.site.register(data_stealer.models.Price)
admin.site.register(data_stealer.models.ClothesType)
admin.site.register(data_stealer.models.Clothes)


