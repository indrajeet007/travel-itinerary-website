from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import RegistrationModel
# Create your views here.
def index(request):
    return render(request,'index.html')
def sample(request):
    return HttpResponse('<h1>Welcome</h1>')
def register(request):
    if request.method == "POST":
        if request.POST.get('regbut'):
            uname=request.POST.get('username')
            email=request.POST.get('email')
            pwd=request.POST.get('password')
            fname=request.POST.get('first_name')
            lname=request.POST.get('last_name')
           # gender=request.POST.get('gender')
            form=RegistrationModel(uname, email, pwd, fname, lname) #constructor for storing data into model
            form.save()
            HttpResponseRedirect("/")




