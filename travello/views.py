from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):    
    
    # dest1 = Destination()
    # dest1.name = 'Mumbai'
    # dest1.desc = 'City that never sleeps'
    # dest1.img = 'destination_1.jpg'
    # dest1.price = 7000
    # dest1.offer = False

    # dest2 = Destination()
    # dest2.name = 'Hyderbad'
    # dest2.desc = 'City f Briyani'
    # dest2.img = 'destination_2.jpg'
    # dest2.price = 5000
    # dest2.offer = True

    # dest3 = Destination()
    # dest3.name = 'Pune'
    # dest3.desc = 'City of Education'
    # dest3.img = 'destination_3.jpg'
    # dest3.price = 6000
    # dest3.offer = False

    # dests = [dest1, dest2, dest3]

    dests = Destination.objects.all()

    return render(request,'index.html',{'dests': dests})
    #return render(request,'index.html',{'dest1': dest1})
    #return render(request,'index.html',{'price': 70130})
