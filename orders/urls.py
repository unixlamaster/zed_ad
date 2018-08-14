from django.conf.urls import url
from . import views


urlpatterns = [
    url('/orders/login', views.login, name="order_login"),
    url(r'^$', views.index, name="order_index_url"),
]