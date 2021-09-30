# -*- coding: utf-8 -*-
# @Time    : 2021/8/23 8:31 下午
# @Author  : Delock
from django.urls import path, include

from shoppingcars import views

urlpatterns = [
    path('latest-products/', views.LatesProductsList.as_view()),
    path('products/search/', views.search),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetails.as_view()),


]
