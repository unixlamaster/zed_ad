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

def prices_asJson(request):
#    import pdb; pdb.set_trace()
    from django.forms.models import model_to_dict
    import logging
    logger = logging.getLogger(__name__)
    logger.error(request.GET['search[value]'])
    pre_data = Price.objects.filter(oemnumber__iregex=r""+request.GET['search[value]'])
    logger.error(pre_data)
    pprice_list=[]
    for p in pre_data:
        d = model_to_dict(p)
        if len(d['oemnumber'])>40:
            d['oemnumber']=d['oemnumber'][:40]+"..."
        d['link'] = "<a href=#><i class='fa fa-shopping-cart' style='font-size: 20px;'></i></a>"
        pprice_list.append(d)
    respons = {
        "draw":request.GET['draw'],
        "recordsTotal":100,
        "recordsFiltered": 10,
        "data": pprice_list
    }
#    logger.error(JsonResponse(respons, safe=False))
    return JsonResponse(respons, safe=False)