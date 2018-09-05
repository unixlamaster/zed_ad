from django.conf.urls import url
from . import views


urlpatterns = [
    url('confirm', views.confirm_order_view, name="confirm_order_url"),
    url(r'^$', views.index_view, name="order_index_url"),
]