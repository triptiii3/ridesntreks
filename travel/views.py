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