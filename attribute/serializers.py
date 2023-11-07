from rest_framework import serializers
from attribute import models


class AttributeOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AttributeOption
        fields = ("id", "title", "order")


class AttributeSerializer(serializers.ModelSerializer):
    options = AttributeOptionSerializer(many=True, read_only=True)

    class Meta:
        model = models.Attribute
        fields = (
            "id",
            "title",
            "image",
            "options",
            "type",
            "is_required",
            "is_list",
            "is_filter",
            "order",
        )


class FilterAttributeSerializer(serializers.ModelSerializer):
    options = AttributeOptionSerializer(many=True, read_only=True)

    class Meta:
        model = models.Attribute
        fields = (
            "id",
            "title",
            "image",
            "options",
            "type",
            "filter_type",
            "is_required",
            "is_list",
            "is_filter",
            "order",
        )
