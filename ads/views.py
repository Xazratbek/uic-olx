from typing import Any
from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from ads.serializers import *
from ads.models import Ads, Category, SubCategory, AdsAttributeValue
from attribute.models import Attribute
from rest_framework.response import Response
from django.db.models import Prefetch
from rest_framework import status
from django_filters import rest_framework as filters
import django_filters


class AdsAttributeValueView(generics.ListAPIView):
    queryset = AdsAttributeValue.objects.all()
    serializer_class = AdsAttributeValueSerializer


class MainCategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FilterCategoryListView(generics.ListAPIView):
    queryset = Category.objects.all().prefetch_related(
        Prefetch(
            "subcategory",
            queryset=SubCategory.objects.all().prefetch_related(
                Prefetch(
                    "attributes",
                    queryset=Attribute.objects.filter(is_filter=True),
                )
            ),
        )
    )
    serializer_class = FilterCategorySerializer
    filterset_fields = [
        "title",
    ]


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AdsTopView(generics.ListAPIView):
    queryset = Ads.objects.filter(is_top=True)
    serializer_class = AdsSerializer


class AdsListView(generics.ListAPIView):
    sub_category = FilterCategoryListView()
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    attribute_values = AdsAttributeValueView()
    search_fields = ["title"]
    filterset_fields = [
        "sub_category",
        "district",
        "attribute_values",
        "is_top",
        "is_vip",
        "price",
        "currency",
    ]


class AdsImageViev(generics.ListAPIView):
    queryset = models.AdsImage.objects.all()
    serializer_class = AdsImageSerializer


class VIPAdsView(generics.ListAPIView):
    serializer_class = AdsSerializer

    def get_queryset(self):
        return Ads.objects.filter(is_vip=True)


class FilterCategoryListView(generics.ListAPIView):
    queryset = Category.objects.all().prefetch_related(
        Prefetch(
            "subcategory",
            queryset=SubCategory.objects.all().prefetch_related(
                Prefetch(
                    "attributes",
                    queryset=Attribute.objects.filter(is_filter=True),
                )
            ),
        )
    )
    serializer_class = FilterCategorySerializer


class AdsCreateView(generics.CreateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer


class AdsDetailView(generics.RetrieveAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        user_has_viewed = request.session.get(f"viewed_ads_{instance.pk}", False)

        if not user_has_viewed:
            instance.views += 1
            instance.save()
            request.session[f"viewed_ads_{instance.pk}"] = True

        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AdsUpdateView(generics.UpdateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer


class AdsDeleteView(generics.DestroyAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer


class AdsCategorySubcategoryListView(generics.ListAPIView):
    serializer_class = AdsCategorySubcategorySerializer
    filterset_fields = [
        "sub_category",
        "district",
        "is_top",
        "is_vip",
        "price",
        "currency",
    ]

    def get_queryset(self):
        category_slug = self.kwargs.get("category_slug")
        subcategory_slug = self.kwargs.get("subcategory_slug")
        return Ads.objects.filter(
            sub_category__category__slug=category_slug,
            sub_category__slug=subcategory_slug,
        )


class AdsCategorySerializerListView(generics.ListAPIView):
    serializer_class = AdsCategorySerializer
    sub_category = SubCategorySerializer
    filterset_fields = [
        "sub_category",
        "district",
        "is_top",
        "is_vip",
        "price",
        "currency",
    ]

    def get_queryset(self):
        category_slug = self.kwargs.get("category_slug")
        return Ads.objects.filter(
            sub_category__category__slug=category_slug,
        )


# class AdsRUDView(generics.RetrieveUpdateDestroyAPIView):
#     """RUD => Retrieve Update Destroy"""

#     queryset = Ads.objects.all()
#     serializer_class = AdsSerializer
