from django.shortcuts import render
from django.http import HttpResponse
from .forms import usersform
from .models import users
def home(request):
    context ={}
    form = usersform(request.POST or None, request.FILES or None)
    context['form']= form
    if form.is_valid():
        form.save()
        b = users.objects.all()
        return render(request,'index.html',{'dblist':b})
    else:
        return render(request, "pluto.html", context)