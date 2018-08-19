from django.conf.urls import url
from . import views


urlpatterns = [
    url('login', views.login_view, name="order_login_url"),
    url('logout', views.logout_view, name="order_logout_url"),
    url('registration', views.registration_view, name="order_registration_url"),
    url(r'^$', views.index_view, name="order_index_url"),
]