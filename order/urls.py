# -*- coding: utf-8 -*-
# @Time    : 2021/8/31 4:44 下午
# @Author  : Delock
from django.urls import path

from order import views

urlpatterns = [
    path('checkout/', views.checkout1),
    path('orders/', views.OrdersList.as_view()),
]
