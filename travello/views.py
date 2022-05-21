from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    #below line sends Http Response to client
    #return HttpResponse('<h1>Welcome to Travello</h1>')

    #below line renders home.html in templates folder
    #return render(request,'home.html',{'username':'John'})

    if request.method=="GET":
        return render(request,'login.html')
    elif request.method=='POST':
        uname=request.POST['username']
        pwd=request.POST['password']
        if uname.lower()=='admin' and pwd=='123':
            return render(request,'home.html',{'username':uname})
        else:
            return HttpResponse('<h1>Invalid user</h1> ')

def view_profile(request):
    pass

def edit_profile(request):
    pass

def delete_profile(request):
    pass