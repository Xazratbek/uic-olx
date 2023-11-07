from django.contrib import admin

from .models import *


class AdsImageInline(admin.TabularInline):
    model = AdsImage


class CustomAdsAdmin(admin.ModelAdmin):
    list_display = ["title"]
    inlines = [AdsImageInline]


# # Register your models here.
admin.site.unregister(Ads)
admin.site.unregister(AdsImage)
admin.site.unregister(Category)
admin.site.unregister(SubCategory)
admin.site.unregister(AdsAttributeValue)
admin.site.unregister(AdsAttributeValueOption)
admin.site.unregister(TopSubscription)
admin.site.unregister(Currency)
admin.site.register(Ads, CustomAdsAdmin)
admin.site.register(AdsImage)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(AdsAttributeValue)
admin.site.register(AdsAttributeValueOption)
admin.site.register(TopSubscription)
admin.site.register(Currency)
