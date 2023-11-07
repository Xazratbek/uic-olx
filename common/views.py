from django.shortcuts import render
from .serializers import RegionSerializer, DistrictSerializer
from rest_framework.generics import ListAPIView
from .models import *
from django.db.models import Prefetch


class RegionSerializerView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class DistrictListAPIView(ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
