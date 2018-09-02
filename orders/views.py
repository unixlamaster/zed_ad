from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from catalog.models import UserSession,Price
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
import logging

def login_view(request):
    logger = logging.getLogger(__name__)
    logger.error("--------------")
    logger.error(request.POST)
    login_alert = 0
    if bool(request.POST):
        user = authenticate(username=request.POST['login'], password=request.POST['password'])
        if user is not None and user.is_active:
            login(request, user)
            return redirect('/orders')
        login_alert = 1
    template = loader.get_template('auth.htm')
    context = {
        '1': 1,
        'title_html': "Hi",
        'body_html': "Site",
        'login_alert': login_alert,
    }
    return HttpResponse(template.render(context, request))
    
def logout_view(request):
    logout(request)
    return redirect('/orders/login')

def registration_view(request):
    input_errors=[]
    if bool(request.POST):
        username = equest.POST['login']
        password=request.POST['password']
        if not password==request.POST['password2']:
            input_errors.append("password_mismatch")
        else:
            try:
                user = User.objects.get(username=username)
            except DoesNotExist:
                newuser = User.objects.create(username=username,password=password,email=username)
                
            else:
                input_errors.append("email_exist")
            
        if user is not None and user.is_active:
            login(request, user)
            return redirect('/orders')
        login_alert = 1
    
    template = loader.get_template('registration.htm')
    context = {
           '1': 1,
           'title_html': "Hi",
           'body_html': "Site",
           "input_errors": input_errors
       }
    return HttpResponse(template.render(context, request))
    
@login_required
def index_view(request):
    data_basket=[]
    summa = 0
    try:
        basket_session = request.session['basket']
    except KeyError:
        basket_session = {}
    index=0
    for priceid in basket_session:
        item = Price.objects.get(id=priceid)
        row = [item.nomenclature,item.describe,item.cost]
        index+=1
        row.append(basket_session[priceid])
        summa+=basket_session[priceid]*item.cost
        row.append(basket_session[priceid]*item.cost)
        data_basket.append(row)
        
    template = loader.get_template('orders.htm')
    context = {
           '1': 1,
           'title_html': "Hi",
           'body_html': "Site",
           'data_basket': data_basket,
           'summa': round(summa,2),
       }
#    logger = logging.getLogger(__name__)
#    logger.error("--------------")
    return HttpResponse(template.render(context, request))

def confirm_order_view(request):
    template = loader.get_template('confirm_order.htm')
    context = {
               'title_html': "Hi",
               'response': "Заказ оформлен",
            }
    return HttpResponse(template.render(context, request))

