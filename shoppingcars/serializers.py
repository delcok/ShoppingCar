# -*- coding: utf-8 -*-
# @Time    : 2021/8/23 7:50 下午
# @Author  : Delock
from rest_framework import serializers

from .models import Category, Product


class ProductSerizlizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail"
        )


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerizlizer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products"
        )
