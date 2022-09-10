from django.shortcuts import render
from django.contrib import messages
from home.models import *
# Create your views here.
def index(request):
   
    popularData=populartrip.objects.all()
    data={
         'popularData':popularData
    }
    return render(request, 'index.html',data)

def popularit(request,id):
    
    popularData=populartrip.objects.filter(id=id)
    data={
        'popularData': popularData
    }
    return render(request,'popularit.html',data)
def checkout(request):
    
    name=request.GET.get('name')
    email=request.GET.get('email')
    people=request.GET.get('people')
    mode=request.GET.get('mode')
    batch=request.GET.get('batch')
    destination=request.GET.get('destination')
    
    data={
        'name':name,'email':email,'people':people,'mode':mode,'batch':batch,'destination':destination
    }
   
    
    return render(request, 'checkout.html',data)
def navigation(request):
    return render(request, 'navigation.html')
def contactus(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']

        if len(name)<2 or len(email)<3 or len(phone)<10 :
            messages.error(request, "Please fill the form correctly")
        else:
           contact=Contact(name=name,email=email,phone=phone,message=message)
           contact.save()
           messages.success(request,"We will reach to you shortly.")
    return render(request, 'contactus.html')
def roadit(request,id):
    
    roadtourData=roadtrip.objects.filter(id=id)
    data={
        'roadtourData': roadtourData
    }
    return render(request,'roadit.html',data)
def roadtours(request):
    roadtourData=roadtrip.objects.all()
    if request.method=="GET":
        st=request.GET.get('destinationname')
        if st!=None:
            roadtourData=roadtrip.objects.filter(destination_title__icontains= st)
    
    data={
        'roadtourData':roadtourData
    }
    return render(request, 'roadtours.html',data)
def bikingit(request,id):
    
    bikingtourData=bikingtrip.objects.filter(id=id)
    data={
        'bikingtourData': bikingtourData
    }
    return render(request,'bikingit.html',data)
def bikingtours(request):
    bikingtourData=bikingtrip.objects.all()
    if request.method=="GET":
        st=request.GET.get('destinationname')
        if st!=None:
            bikingtourData=bikingtrip.objects.filter(destination_title__icontains= st)
    
    data={
        'bikingtourData':bikingtourData
    }
    return render(request, 'bikingtours.html',data)
def spitiit(request,id):
    
    spitiData=spititrip.objects.filter(id=id)
    data={
        'spitiData': spitiData
    }
    return render(request,'spitiit.html',data)
def spititours(request):
    spitiData=spititrip.objects.all()
    if request.method=="GET":
        st=request.GET.get('destinationname')
        if st!=None:
            spitiData=spititrip.objects.filter(destination_title__icontains= st)
    
    data={
        'spitiData':spitiData
    }
    return render(request, 'spititours.html',data)
def lehit(request,id):
    
    lehData=lehtrip.objects.filter(id=id)
    data={
        'lehData': lehData
    }
    return render(request,'lehit.html',data)
def lehtours(request):
    lehData=lehtrip.objects.all()
    if request.method=="GET":
        st=request.GET.get('destinationname')
        if st!=None:
            lehData=lehtrip.objects.filter(destination_title__icontains= st)
    
    data={
        'lehData':lehData
    }
    return render(request, 'lehtours.html',data)
def himachalit(request,id):
    
    himachalData=himachaltrip.objects.filter(id=id)
    data={
        'himachalData': himachalData
    }
    return render(request,'himachalit.html',data)
def himachaltours(request):
    himachalData=himachaltrip.objects.all()
    if request.method=="GET":
        st=request.GET.get('destinationname')
        if st!=None:
            himachalData=himachaltrip.objects.filter(destination_title__icontains= st)
    
    data={
        'himachalData':himachalData
    }
    return render(request, 'himachaltours.html',data)
def bhutanit(request,id):
    
    bhutanData=bhutantrip.objects.filter(id=id)
    data={
        'bhutanData': bhutanData
    }
    return render(request,'bhutanit.html',data)
def bhutantours(request):
    bhutanData=bhutantrip.objects.all()
    if request.method=="GET":
        st=request.GET.get('destinationname')
        if st!=None:
            bhutanData=bhutantrip.objects.filter(destination_title__icontains= st)
    
    data={
        'bhutanData':bhutanData
    }
    return render(request, 'bhutantours.html',data)
def dubaiit(request,id):
    
    dubaiData=dubaitrip.objects.filter(id=id)
    data={
        'dubaiData': dubaiData
    }
    return render(request,'dubaiit.html',data)
def dubaitours(request):
    dubaiData=dubaitrip.objects.all()
    if request.method=="GET":
        st=request.GET.get('destinationname')
        if st!=None:
            dubaiData=dubaitrip.objects.filter(destination_title__icontains= st)
    
    data={
        'dubaiData':dubaiData
    }
    return render(request, 'dubaitours.html',data)
def kashmirit(request,id):
    
    kashmirData=kashmirtrip.objects.filter(id=id)
    data={
        'kashmirData': kashmirData
    }
    return render(request,'kashmirit.html',data)
def kashmirtours(request):
    kashmirData=kashmirtrip.objects.all()
    if request.method=="GET":
        st=request.GET.get('destinationname')
        if st!=None:
            kashmirData=kashmirtrip.objects.filter(destination_title__icontains= st)
    
    data={
        'kashmirData':kashmirData
    }
    return render(request, 'kashmirtours.html',data)
def sikkimit(request,id):
    
    sikkimData=sikkimtrip.objects.filter(id=id)
    data={
        'sikkimData': sikkimData
    }
    return render(request,'sikkimit.html',data)
def sikkimtours(request):
    sikkimData=sikkimtrip.objects.all()
    if request.method=="GET":
        st=request.GET.get('destinationname')
        if st!=None:
         sikkimData=sikkimtrip.objects.filter(destination_title__icontains= st)
     
    data={
        'sikkimData':sikkimData
    }
    return render(request, 'sikkimtours.html',data)
def meghalayait(request,id):
    
    meghalayaData=meghalayatrip.objects.filter(id=id)
    data={
        'meghalayaData': meghalayaData
    }
    return render(request,'meghalayait.html',data)
def meghalayatours(request):
    meghalayaData=meghalayatrip.objects.all()
    if request.method=="GET":
        st=request.GET.get('destinationname')
        if st!=None:
         meghalayaData=meghalayatrip.objects.filter(destination_title__icontains= st)
     
    data={
        'meghalayaData':meghalayaData
    }
    return render(request, 'meghalayatours.html',data)
def backpackit(request,id):
    
    backpackData=backpackingtrip.objects.filter(id=id)
    data={
        'backpackData': backpackData
    }
    return render(request,'backpackit.html',data)
def backpackingtours(request):
    backpackData=backpackingtrip.objects.all()
    if request.method=="GET":
        st=request.GET.get('destinationname')
        if st!=None:
            backpackData=backpackingtrip.objects.filter(destination_title__icontains= st)
    
    data={
        'backpackData':backpackData
    }
    return render(request, 'backpackingtours.html',data)
def weekendtours(request):
    weekendData=weekendtrip.objects.all()
    if request.method=="GET":
        st=request.GET.get('destinationname')
        if st!=None:
            weekendData=weekendtrip.objects.filter(destination_title__icontains= st)
    
    data={
        'weekendData':weekendData
    }
    return render(request, 'weekendtours.html',data)
def weekendit(request,id):
    
    weekendData=weekendtrip.objects.filter(id=id)
    data={
        'weekendData': weekendData
    }
    return render(request,'weekendit.html',data)
def treks(request):
    treksData=firsts.objects.all()
    if request.method=="GET":
        st=request.GET.get('destinationname')
        if st!=None:
            treksData=firsts.objects.filter(destination_title__icontains= st)
    
    data={
        'treksData':treksData
    }
    return render(request, 'treks.html')
def treksit(request,id):
    treksData=firsts.objects.filter(id=id)
    data={
        'treksData': treksData
    }
    return render(request,'treksit.html',data)
def alltours(request):
    alltoursData=alltrip.objects.all()
    if request.method=="GET":
        st=request.GET.get('destinationname')
        if st!=None:
            alltoursData=alltrip.objects.filter(destination_title__icontains= st)
    
    data={
        'alltoursData':alltoursData
    }
    return render(request, 'alltours.html',data)
def alltoursit(request,id):
    
    alltoursData=alltrip.objects.filter(id=id)
    data={
        'alltoursData': alltoursData
    }
    return render(request,'alltoursit.html',data)