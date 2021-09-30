"""Myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

from product.views import home_view, product_create_view

from blog.views import blog_view, cv_view, write_view
urlpatterns = [
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('shoppingcars.urls')),
    path('api/v1/', include('order.urls')),


    path('admin/', admin.site.urls),
    path('blog/', blog_view, name='index'),
    path('write/', write_view, name="write"),
    path('', cv_view, name='cv'),
    path('test/', home_view, name='home'),
    path('pro/', product_create_view, name="create"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
