from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from catalog.models import Price

def index(request):
#    return HttpResponse("<h2>Hi !!!</h2>")
    template = loader.get_template('main.htm')
    context = {
        '1': 1,
        'title_html': "Hi",
        'body_html': "Site",
    }
#    return render(request, 'main.htm')
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
    import logging
    logger = logging.getLogger(__name__)
    logger.error(request.GET)
    pages = Paginator(Price.objects.filter(Q(oemnumber__iregex=r""+request.GET['search[value]']) | Q(nomenclature__iregex=r""+request.GET['search[value]']) | Q(articul__iregex=r""+request.GET['search[value]']) | Q(describe__iregex=r""+request.GET['search[value]'])).order_by(sorted_field(request)),int(request.GET['length']))
    pre_data = pages.page(int(request.GET['start'])/int(request.GET['length']) + 1)
    logger.error(pre_data)
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