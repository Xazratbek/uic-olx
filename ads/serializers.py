from rest_framework import serializers
from ads import models
from common.serializers import DistrictSerializer
from attribute.serializers import (
    AttributeOptionSerializer,
    AttributeSerializer,
    FilterAttributeSerializer,
)


class AdsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AdsImage
        fields = ("id", "image")


# class TopAds
class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Currency
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ("id", "title", "ads_count", "image")


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = models.SubCategory
        fields = (
            "id",
            "title",
            "category",
            "ads_count",
        )


class FilterSubCategorySerializer(serializers.ModelSerializer):
    attributes = FilterAttributeSerializer(many=True)

    class Meta:
        model = models.SubCategory
        fields = ("id", "title", "ads_count", "category", "attributes")


class FilterCategorySerializer(serializers.ModelSerializer):
    subcategory = FilterSubCategorySerializer(many=True)

    class Meta:
        model = models.Category
        fields = ("id", "title", "ads_count", "image", "subcategory")


####
class AdsAttributeValueOption(serializers.ModelSerializer):
    option = AttributeOptionSerializer()

    class Meta:
        model = models.AdsAttributeValueOption
        fields = (
            "id",
            "option",
        )


class AdsAttributeValueSerializer(serializers.ModelSerializer):
    value_options = AdsAttributeValueOption(many=True)
    attribute = AttributeSerializer()

    class Meta:
        model = models.AdsAttributeValue
        fields = ("id", "attribute", "value_options", "value")


class AdsSerializer(serializers.ModelSerializer):
    image = AdsImageSerializer(many=True, read_only=True)
    sub_category = SubCategorySerializer()
    district = DistrictSerializer()
    currency = CurrencySerializer()
    # attributes = AdsAttributeValueSerializer

    attribute_values = AdsAttributeValueSerializer(many=True, required=False)

    class Meta:
        model = models.Ads
        fields = (
            "id",
            "title",
            "price",
            "is_top",
            "is_vip",
            "sub_category",
            "district",
            "address",
            "attribute_values",
            "created_at",
            "updated_at",
            "views",
            "currency",
            "image",
        )


class AdsCategorySubcategorySerializer(serializers.ModelSerializer):
    district = DistrictSerializer()

    attribute_values = AdsAttributeValueSerializer(many=True, required=False)
    category = serializers.StringRelatedField(
        source="sub_category.category", read_only=True
    )
    subcategory = serializers.StringRelatedField(source="sub_category", read_only=True)
    currency = CurrencySerializer()

    class Meta:
        model = models.Ads
        fields = (
            "id",
            "title",
            "image",
            "price",
            "is_top",
            "is_vip",
            "subcategory",
            "category",
            "district",
            "address",
            "attribute_values",
            "created_at",
            "updated_at",
            "views",
            "currency",
        )


class AdsCategorySerializer(serializers.ModelSerializer):
    district = DistrictSerializer()
    attribute_values = AdsAttributeValueSerializer(many=True, required=False)
    category = serializers.StringRelatedField(
        source="sub_category.category", read_only=True
    )
    subcategory = serializers.StringRelatedField(source="sub_category", read_only=True)
    currency = CurrencySerializer()

    class Meta:
        model = models.Ads
        fields = (
            "id",
            "title",
            "image",
            "price",
            "is_top",
            "is_vip",
            "subcategory",
            "category",
            "district",
            "address",
            "attribute_values",
            "created_at",
            "updated_at",
            "views",
            "currency",
        )
