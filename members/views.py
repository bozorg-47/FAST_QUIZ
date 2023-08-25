from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member


def members(request):
    mymembers = Member.objects.all().values()                # data ra az databse megira
    template = loader.get_template('all_members.html')   
    context = {
    'mymembers': mymembers,
  }
    return HttpResponse(template.render(context, request))


def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))





def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())


def football(request):
    template = loader.get_template('football.html')
    return HttpResponse(template.render())

def general(request):
    template = loader.get_template('general.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())