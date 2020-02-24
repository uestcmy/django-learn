from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from ArpApp import models
from ArpApp.models import Device

def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hellot.html', context)

def show_homepage(request):
    return render(request, 'homepage.html')

# 接收POST请求数据
def add_dev(request):
    ctx = {}
    if request.POST:
        d_name_p = request.POST.get("dev_name",None)
        ip_p = request.POST.get("ip", None)
        vendor_p = request.POST.get("vendor", None)
        model_p = request.POST.get("model",None)
        series_p = request.POST.get("series", None)
        #print(ip_p)

        dev1 = Device(ip = ip_p, dev_name = d_name_p, vendor = vendor_p, model = model_p, series = series_p)
        dev1.save()

        '''
        models.Device.objects.create(
            ip=ip_p,
            #dev_name = d_name_p,
            vendor = vendor_p
        )
        '''
        dev_info_list = models.Device.objects.all()

        return render(request, "dev_list.html", {"dev_info_list": dev_info_list})

    return render(request, "dev_add.html", ctx)

def show_dev(request):
    dev_info_list = models.Device.objects.all()
    return render(request, "dev_list.html", {"dev_info_list": dev_info_list})