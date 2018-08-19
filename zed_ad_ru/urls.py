"""zed_ad_ru URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from catalog import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('orders/', include('orders.urls')),
    path('prices/', views.prices_asJson, name="my_price_data_url"),
    path('basket/index', views.basketList_asJson, name="my_basket_data_url"),
    path('basket/itemadd', views.basket_item_addJson, name="basket_item_add_url"),
    path('basket/itemdel', views.basket_item_delJson, name="basket_item_del_url"),
    url(r'^accounts/', include('allauth.urls')),
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]
