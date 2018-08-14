from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from catalog.models import UserSession,Price
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session
from django.forms.models import model_to_dict
import logging

def login(request):
	template = loader.get_template('auth.htm')
	context = {
		'1': 1,
		'title_html': "Hi",
		'body_html': "Site",
        'login_alert': 0,
	}
	return HttpResponse(template.render(context, request))    

def index(request):
	logger = logging.getLogger(__name__)
    if not request.user.is_authenticated():
        return redirect('/orders/login')
	user = authenticate(username=request.POST['login'], password=request.POST['password']) if request.method == "POST" else None
	if user is not None:
		# A backend authenticated the credentials
		template = loader.get_template('orders.htm')
		context = {
			'1': 1,
			'title_html': "Hi",
			'body_html': "Site",
		}
	else:
		# No backend authenticated the credentials
		template = loader.get_template('auth.htm')
		context = {
			'1': 1,
			'title_html': "Hi",
			'body_html': "Site",
            'login_alert': 0,
		}
#    return render(request, 'main.htm')
	logger.error("--------------")
#    check_session(request)
	return HttpResponse(template.render(context, request))

# Create your views here.
