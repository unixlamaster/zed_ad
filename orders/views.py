from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
import logging
from catalog.models import UserSession,Price
from orders.models import Order,OrderItem
from django.core.mail import EmailMultiAlternatives
   
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
           'data_basket': zip(range(1,len(data_basket)+1),data_basket),
           "basket_menu_show": True,
           'summa': round(summa,2),
       }
#    logger = logging.getLogger(__name__)
#    logger.error("--------------")
    return HttpResponse(template.render(context, request))

def send_order2email(order_id):
    data_basket=[]   
    summa = 0
    template = loader.get_template('order2email.htm')
    subject = "Order №"+str(order_id)
    order = Order.objects.get(id=order_id)
    order_items = order.orderitem_set.all()
    index=0
    for item in order_items:
        summa+=item.count*item.cost
        data_basket.append([item.nomenclature,item.articul,item.cost,item.count,item.count*item.cost])
    context = { 'order_items': zip(range(1,len(data_basket)+1),data_basket),
                "order_id": order_id,
                "summa": round(summa,2),
                 "user": order.user.first_name+" "+order.user.last_name+" ("+order.user.username+")" }
    html_content = template.render(context)
    msg = EmailMultiAlternatives(subject, "", "", ["unixlamaster@mail.ru"])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    
def confirm_order_view(request):
    data_basket=[]   
    summa = 0
    order = Order(user=request.user,status="new",summa_invoice=0)
    order.save()
    try:
        basket_session = request.session['basket']
    except KeyError:
        basket_session = {}
    index=0
    for priceid in basket_session:
        item = Price.objects.get(id=priceid)
        OrderItem.objects.create(order=order,priceitem=item,cost=item.cost,count=basket_session[priceid],provider=item.provider,nomenclature=item.nomenclature,brend=item.brend,articul=item.articul)
        summa+=basket_session[priceid]*item.cost
    order.summa_invoice = round(summa,2)
    order.save()
    send_order2email(order.id)
    request.session['basket'] = {}
    template = loader.get_template('confirm_order.htm')
    context = {
               'title_html': "Hi",
               'user': "Пользователь: "+request.user.username,
               'response': "Ваш заказ №"+str(order.id)+" оформлен",
            }
    return HttpResponse(template.render(context, request))

