"""ridesntreks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from travel.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('navigation', navigation ,name="navigation"),
    path('contactus', contactus ,name="contactus"),
    path('bikingtours', bikingtours ,name="bikingtours"),
    path('spititours', spititours ,name="spititours"),
    path('roadtours', roadtours ,name="roadtours"),
    path('lehtours', lehtours ,name="lehtours"),
    path('bhutantours', bhutantours ,name="bhutantours"),
    path('dubaitours', dubaitours ,name="dubaitours"),
    path('kashmirtours', kashmirtours ,name="kashmirtours"),
    path('sikkimtours', sikkimtours ,name="sikkimtours"),
    path('meghalayatours', meghalayatours ,name="meghalayatours"),
    path('himachaltours', himachaltours ,name="himachaltours"),
    path('treks', treks ,name="treks"),
    path('checkout', checkout ,name="checkout"),
    path('privacy', privacy ,name="privacy"),
    path('aboutus', aboutus ,name="aboutus"),

    path('backpackingtours', backpackingtours ,name="backpackingtours"),
    path('weekendtours', weekendtours ,name="weekendtours"),
    path('alltours', alltours ,name="alltours"),
    path('treks/<int:id>', treksit ,name="treksit"),
    path('alltours/<int:id>', alltoursit ,name="alltoursit"),
    path('weekendtours/<int:id>', weekendit ,name="weekendit"),
    path('backpackingtours/<int:id>', backpackit ,name="backpackit"),
    path('roadtours/<int:id>', roadit ,name="roadit"),
    path('bikingtours/<int:id>', bikingit ,name="bikingit"),
    path('spititours/<int:id>', spitiit ,name="spitiit"),
    path('dubaitours/<int:id>', dubaiit ,name="dubaiit"),
    path('lehtours/<int:id>', lehit ,name="lehit"),
    path('himachaltours/<int:id>', himachalit ,name="himachalit"),
    path('bhutantours/<int:id>', bhutanit ,name="bhutanit"),
    path('kashmirtours/<int:id>', kashmirit ,name="kashmirit"),
    path('sikkimtours/<int:id>', sikkimit ,name="sikkimit"),
    path('meghalayatours/<int:id>', meghalayait ,name="meghalayait"),
     path('index/<int:id>', popularit ,name="popularit"),
    
]
urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
