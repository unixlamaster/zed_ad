from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name="order_index_url"),
]