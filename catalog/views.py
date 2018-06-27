from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

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