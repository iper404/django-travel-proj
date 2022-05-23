from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . import models
from .models import Destination
from .forms import DestinationForm

def homepage(request):
    dests=Destination.objects.all()
    return render(request,'index.html',{'dests':dests})

    #below line sends Http Response to client
    #return HttpResponse('<h1>Welcome to Travello</h1>')

    #below line renders home.html in templates folder
    #return render(request,'home.html',{'username':'John'})

    # if request.method=="GET":
    #     return render(request,'login.html')
    # elif request.method=='POST':
    #     uname=request.POST['username']
    #     pwd=request.POST['password']
    #     if uname.lower()=='admin' and pwd=='123':
    #         return render(request,'home.html',{'username':uname})
    #     else:
    #         return HttpResponse('<h1>Invalid user</h1> ')
    # dest=models.Destination()
    # dest.id=1
    # dest.name='Hyderabad'
    # dest.desc='The Ethnic City'
    # dest.img='destination_1.jpg'
    # dest.price=500
    # return render(request,'index.html',{'dest1':dest})

def dest_details(request,id):
    dest=list(Destination.objects.filter(id=id))[0]
    if dest:
        d=request.COOKIES.setdefault('recent_destinations','')
        if dest.name not in d.split('\n'):
            d=d+'\n'+dest.name
            d=d.strip('\n')
        response = render(request, 'destination.html', {'dest':dest})
        response.set_cookie('recent_destinations',d)
        #return render(request,'destination.html',{'dest':dest[0]})
        return response

def dest_add(request):
    if request.method=='POST':
        form = DestinationForm(request.POST,request.FILES)
        print(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            messages.info(request,'Error while creating Destination')
    return render(request,'destinationForm.html',{'form':DestinationForm()})



def view_profile(request):
    pass

def edit_profile(request):
    pass

def delete_profile(request):
    pass