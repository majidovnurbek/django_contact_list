from django.shortcuts import render
from apps.models import Person,Job

def index(request):
    posts = Person.objects.all()
    return render(request,'contact.html', {'posts': posts})