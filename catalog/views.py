from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from catalog.models import UserSession,Price
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
import logging

def check_session(request):
    logger = logging.getLogger(__name__)
    if not request.session.session_key:
        request.session.save()
    session_id = request.session.session_key
    logger.error(session_id)
#        user = User.objects.get(id=2)
#        logger.error(request.session.model()) 
#        snew = UserSession(user=user,session=request.session.model())
##        snew.save()
#        logger.error(snew.id)   
#        id = request.session['id'] = snew.id

    
def index(request):
#    return HttpResponse("<h2>Hi !!!</h2>")
    logger = logging.getLogger(__name__)
    template = loader.get_template('main.htm')
    context = {
        '1': 1,
        'title_html': "Hi",
        'body_html': "Site",
    }
#    return render(request, 'main.htm')
    logger.error("--------------")
#    check_session(request)
    return HttpResponse(template.render(context, request))
    
def prices(request):
#    return HttpResponse("<h2>Hi !!!</h2>")
    template = loader.get_template('prices.htm')
    context = {
        '1': 1,
        'title_html': "Prices",
        'body_html': "Site",
    }
#    return render(request, 'main.htm')
    return HttpResponse(template.render(context, request))

def sorted_field(request):
    fields = ['nomenclature', 'brend', 'articul', 'describe', 'cost', 'catnumber', 'oemnumber']
    if request.GET['order[0][dir]'] == 'asc':
        return "-"+fields[int(request.GET['order[0][column]'])]
    else:
        return fields[int(request.GET['order[0][column]'])]

def prices_asJson(request):
#    import pdb; pdb.set_trace()
    from django.forms.models import model_to_dict
    from django.core.paginator import Paginator
    from django.db.models import Q
    
#    logger = logging.getLogger(__name__)
#    logger.error(request.GET)
    pages = Paginator(Price.objects.filter(Q(oemnumber__iregex=r""+request.GET['search[value]']) | Q(nomenclature__iregex=r""+request.GET['search[value]']) | Q(articul__iregex=r""+request.GET['search[value]']) | Q(describe__iregex=r""+request.GET['search[value]'])).order_by(sorted_field(request)),int(request.GET['length']))
    pre_data = pages.page(int(request.GET['start'])/int(request.GET['length']) + 1)
#    logger.error(pre_data)
    pprice_list=[]
    for p in pre_data:
        d = model_to_dict(p)
        if len(d['oemnumber'])>40:
            d['oemnumber']=d['oemnumber'][:40]+"..."
# <i class='fa fa-shopping-cart' style='font-size: 20px;'></i>
        d['link'] = "<a href=# class='fly-to-basket' data-fly-to-basket='#item"+ str(d['id']) +"'><img id=item"+ str(d['id']) +" src=/static/img/basket.png></a>"
        
        pprice_list.append(d)
    respons = {
        "draw":request.GET['draw'],
        "recordsTotal":Price.objects.all().count(),
        "recordsFiltered": pages.count,
        "data": pprice_list
    }
#    logger.error(JsonResponse(respons, safe=False))
    return JsonResponse(respons, safe=False)

def basketList_asJson(request):
    logger = logging.getLogger(__name__)
    logger.error(request.GET)
    data_basket=[]
    try:
        basket_session = request.session['basket']
    except KeyError:
        basket_session = {}
    for priceid in basket_session:
        data_basket.append(model_to_dict(Price.object.get(id=priceid)))
    respons = {
        "recordsTotal":data_basket.count,
        "data": data_basket
    }
    logger.error(JsonResponse(respons, safe=False))
    return JsonResponse(respons, safe=False)
    
def basket_item_addJson(request):
    logger = logging.getLogger(__name__)
    if not request.session.session_key:
        request.session.save()
    session_id = request.session.session_key
    priceid = request.GET['item']
    logger.error(priceid)  
    p_item = Price.objects.get(id=priceid)
    try:
        basket = request.session['basket']
    except KeyError:
        basket = {}
    if type(basket[priceid]) == int:  
        basket[priceid]+=1  
    else:
        basket[priceid] = 0
    request.session['basket'] = basket
    logger.error(session_id)
    
    respons = { 
        "data": [p_item.nomenclature,
                 p_item.brend,
                 p_item.articul,
                 p_item.describe,
                 p_item.multi,
                 p_item.cost,
                 p_item.availability,
                 p_item.delivery,
                 p_item.catnumber,
                 p_item.oemnumber      
                 ]}
    return JsonResponse(respons, safe=False)