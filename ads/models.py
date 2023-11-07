from django.db import models
from utils.models import BaseModel
from django.contrib.auth import get_user_model
from django.utils.text import slugify

# Create your models here.
User = get_user_model()


class TopSubscription(BaseModel):
    basic_subscription = models.BooleanField(default=False)
    pro_subscription = models.BooleanField(default=False)
    vip_subscription = models.BooleanField(default=False)
    no_subscription = models.BooleanField(default=False)

    def __str__(self):
        if self.basic_subscription:
            return "Basic Subscription"
        elif self.pro_subscription:
            return "Pro Subscription"
        elif self.vip_subscription:
            return "VIP Subscription"
        elif self.no_subscription:
            return "No Subscription"
        else:
            return "Unknown Subscription"


class Currency(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Category(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="main_category")
    ads_count = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, auto_created=True, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class SubCategory(BaseModel):
    title = models.CharField(max_length=255)

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="subcategory"
    )
    attributes = models.ManyToManyField("attribute.Attribute", blank=True)

    ads_count = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, auto_created=True, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(SubCategory, self).save(*args, **kwargs)


class Ads(BaseModel):
    title = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    content = models.TextField()
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, related_name="sub_category"
    )
    district = models.ForeignKey("common.District", on_delete=models.CASCADE)
    is_top = models.ForeignKey(TopSubscription, on_delete=models.CASCADE)
    is_vip = models.BooleanField(default=False)
    address = models.CharField(max_length=255, null=True, blank=True)
    depth = 3
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_address_text(self):
        return f"{self.district.region.title}, {self.district.title}"


class AdsImage(models.Model):
    ad = models.ForeignKey(Ads, on_delete=models.CASCADE, related_name="image")
    image = models.ImageField(upload_to="ads_images")


class AdsAttributeValue(BaseModel):
    value = models.CharField(max_length=255, null=True, blank=True)

    ads = models.ForeignKey(
        Ads, on_delete=models.CASCADE, related_name="attribute_values"
    )
    attribute = models.ForeignKey("attribute.Attribute", on_delete=models.CASCADE)

    def __str__(self):
        return self.value


class AdsAttributeValueOption(BaseModel):
    ads_attribute_value = models.ForeignKey(
        AdsAttributeValue, on_delete=models.CASCADE, related_name="value_options"
    )
    option = models.ForeignKey("attribute.AttributeOption", on_delete=models.CASCADE)

    def __str__(self):
        return self.ads_attribute_value.value
