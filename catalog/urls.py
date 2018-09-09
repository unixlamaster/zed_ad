from django.conf.urls import url
from . import views


urlpatterns = [
    url('send_email', views.send_email_Json, name="send_email_url"),
    url(r'^$', views.index),
]