# Uyga vazifa (https://t.me/c/2014071612/216)

# 1. Category.objects.filter(title__istartswith="О")
# 2. Category.objects.filter(title__icontains="avto")
# 3. Category.objects.filter(id__gt=5) yoki Category.objects.all()[5:10]
# 4. Category.objects.filter(created_at__year=2023)
# 5. Category.objects.filter("-updated_at")
# 6. category_title = "Transport"
#    subcategory_title = "Yengil Mashina"
#    ads_title = "matiz"

#    query = Ads.objects.filter(
#        sub_category__category__title__iexact=category_title,
#        sub_category__title__iexact=subcategory_title,
#        title__icontains=ads_title
#    )

# 7.  category_title = "Недвижимост"
#     subcategory_title = "Квартиры"
#     query = Ads.objects.filter(sub_category__category__title__iexact=category_title,sub_category__title__iexact=subcategory_title)

# 8 print(Category.objects.filter(Q(title__icontains="S") | Q(created_at__year=2022)))

# 9. from django.db.models import F
#    ad_id = 1
#    Ads.objects.filter(id=ad_id).update(views=F('views') + 1)

# 10.
# category_title = "Недвижимост"
# subcategory_title = "Квартиры"
# query = Ads.objects.filter(
#     sub_category__category__title__iexact=category_title,
#     sub_category__title__iexact=subcategory_title,
# )
# print(query)  <=> dan qaytgan natija <QuerySet [<Ads: Новостройка ул. Шаумяна ор. Шелкаткацкая 2/7/9 с еврорем. 47м/кв>, <Ads: New Title>, <Ads: Updated Ad Title>, <Ads: New Ad Title>]>

# for product in query:
#     print(product.title.title())

# for loopdan qaytgan natija: Новостройка Ул. Шаумяна Ор. Шелкаткацкая 2/7/9 С Еврорем. 47М/Кв
# New Title
# Updated Ad Title
# New Ad Title


# 11.
#     category_title = "Недвижимост"
#     subcategory_title = "Квартиры"
#     query = Ads.objects.filter(sub_category__category__title__iexact=category_title,sub_category__title__iexact=subcategory_title)
# for product in query:
#     print(product.views)

# 12.
# from django.db.models import Avg, Min, Max, Sum
# from ads.models import Ads

# min_price = Ads.objects.aggregate(min=Min("price"))
# max_price = Ads.objects.aggregate(max=Max("price"))
# average_price = Ads.objects.aggregate(average=Avg("price"))
# summa = Ads.objects.aggregate(sum=Sum("price"))
# print(average_price)

# 13
# from django.db.models import Case, When, F, Sum, Value, DecimalField
# from django.db.models import CharField, IntegerField
# from django.db.models.functions import Cast
# from ads.models import Ads

# price_expression = Case(
#     When(price__range=(100000, 1000000), then=Value(1.0)),
#     When(price__range=(10000, 1000000), then=Value(0.5)),
#     default=Value(0),
#     output_field=DecimalField(),
# )

# district_scores = (
#     Ads.objects.values("district")
#     .annotate(umumiy_narx=Sum(Cast(price_expression, DecimalField())))
#     .values("district", "umumiy_narx")
# )

# district_scores_list = [
#     {"title": entry["district"], "price_res": float(entry["umumiy_narx"])}
#     for entry in district_scores
# ]

# print(district_scores)
