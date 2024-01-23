from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['topic_name']
            To=Topic.objects.get_or_create(topic_name=tn)[0]
            return HttpResponse('Topic is created')
        else:
            return HttpResponse('invalid data')
        
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EWFO=WebPageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebPageForm(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topic_name']
            TO=Topic.objects.get(topic_name=tn)
            n=WFDO.cleaned_data['name']
            u=WFDO.cleaned_data['url']
            g=WFDO.cleaned_data['gmail']
            wo=WebPage.objects.get_or_create(topic_name=TO,name=n,url=u,gmail=g)[0]
            wo.save()
            return HttpResponse('webpage is created')
        else:
            return HttpResponse('invalid data')

    return render(request,'insert_webpage.html',d)


def insert_accessrecord(request):
    EAFO=AccessRecordForm()
    d={'EAFO':EAFO}
    if request.method=='POST':
        AFDO=AccessRecordForm(request.POST)
        if AFDO.is_valid():
            n=AFDO.cleaned_data['name']
            WO=WebPage.objects.get(pk=n) 
            d=AFDO.cleaned_data['date']
            a=AFDO.cleaned_data['author']
            ao=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
            ao.save()
            return HttpResponse('accessrecord is created')
        else:
            return HttpResponse('invalid data')

    return render(request,'insert_accessrecord.html',d)