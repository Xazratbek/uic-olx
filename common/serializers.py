from rest_framework import serializers
from common.models import *


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ("id", "title", "created_at", "updated_at")


class DistrictSerializer(serializers.ModelSerializer):
    region = RegionSerializer()

    class Meta:
        model = District
        fields = ("id", "region", "created_at", "updated_at", "title")
