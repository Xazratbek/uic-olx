from django.urls import path, include
from ads.views import *

urlpatterns = [
    path("", AdsListView.as_view(), name="ads-list"),
    path("create/", AdsCreateView.as_view(), name="ads-create"),
    path("update/<int:pk>/", AdsUpdateView.as_view(), name="ads-update"),
    path("delete/<int:pk>/", AdsDeleteView.as_view(), name="ads-delete"),
    path("<int:pk>/", AdsDetailView.as_view(), name="ads-detail"),
    path("category/", CategoryView.as_view(), name="category"),
    path("top/", AdsTopView.as_view(), name="top-ads"),
    path("category/main/", MainCategoryListView.as_view(), name="ads-list"),
    path("category/filter/", FilterCategoryListView.as_view(), name="ads-list"),
    path(
        "<str:category_slug>/<str:subcategory_slug>/",
        AdsCategorySubcategoryListView.as_view(),
        name="all-category-subcategory-ads",
    ),
    path(
        "<str:category_slug>/",
        AdsCategorySerializerListView.as_view(),
        name="all-category-ads",
    ),
    path("vip/", VIPAdsView.as_view(), name="vip-ads"),
]
