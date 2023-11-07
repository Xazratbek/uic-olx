from django.urls import path
from .views import *

urlpatterns = [
    path("regions/", RegionSerializerView.as_view(), name="regions"),
    path("districts/", DistrictListAPIView.as_view(), name="districts"),
]
