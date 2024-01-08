from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length

# Create your views here.
def display_country(request):
    QLCT=Country.objects.all()
    QLCT=Country.objects.all().order_by('-Country_name') 
    QLCT=Country.objects.all().order_by('Country_name')
   
    d={'country':QLCT}
    return render(request,'country.html',d)


def display_Capital(request):
    QLcT=Capital.objects.all()
    QLcT=Capital.objects.all().order_by('-Capital_name')
    QLcT=Capital.objects.filter(Capital_name__startswith='t').order_by('-Capital_name')
    QLcT=Capital.objects.all().order_by(Length('Country_name'))
    QLcT=Capital.objects.all().order_by(Length('Capital_name').desc())
    QLcT=Capital.objects.all().order_by(Length('Country_name').desc())
    
    d={'capital':QLcT}
    return render(request,'capital.html',d)

