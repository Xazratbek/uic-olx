from django.db import models
from utils.models import BaseModel


class AttributeType(models.TextChoices):
    INTEGER = "integer"  # faqat son kiritiladi
    BUTTON = "button"  # button select
    SELECT = "select"  # ikkitalik tanlov
    MULTISELECT = "multiselect"  # selectli ko'p tanlov


class AttributeFilterType(models.TextChoices):
    RANGE = "range"  # faqat son kiritiladi
    MULTISELECT = "multiselect"  # selectli ko'p tanlov


# Create your models here.
class Attribute(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="category_attributes/", null=True, blank=True)
    type = models.CharField(
        max_length=255, choices=AttributeType.choices, default=AttributeType.INTEGER
    )
    filter_type = models.CharField(
        max_length=255,
        choices=AttributeFilterType.choices,
        default=AttributeFilterType.RANGE,
    )

    is_required = models.BooleanField(default=False)
    is_list = models.BooleanField(default=False)
    is_filter = models.BooleanField(default=False)

    order = models.IntegerField(default=0)

    class Meta:
        ordering = ("order",)

    def __str__(self):
        return self.title


class AttributeOption(BaseModel):
    attribute = models.ForeignKey(
        Attribute, on_delete=models.CASCADE, related_name="options"
    )

    title = models.CharField(max_length=255)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ("order",)

    def __str__(self):
        return self.title
