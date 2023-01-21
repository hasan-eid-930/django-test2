from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members,Teacher,Course,Lecture,Book
import datetime
from django.db.models import Avg,Max,Min,FloatField,Count,Q, F

def index(request):
    members = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'members': members,
    }
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    z = request.POST['date']
    # w = request.POST['datetime']
    age=request.POST['age']
    member = Members(firstname=x, lastname=y,date=z,age=age)
    member.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    member = Members.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'member': member,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    member = Members.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()
    return HttpResponseRedirect(reverse('index'))

def test(request):
    courses=Course.objects.all().values()
    template = loader.get_template('test.html')
    context = {
        'courses':courses
    }
    return HttpResponse(template.render(context, request))