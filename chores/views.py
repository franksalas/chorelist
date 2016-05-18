from django.shortcuts import render
from  django.http import HttpResponse
from .models import ChoreList,Chore
# Create your views here.


def index(request):
    lists = ChoreList.objects.all()
    return render(request, 'chores/index.html', { 'chorelists': lists })


def detail(request, chorelist_id):
    list = ChoreList.objects.get(pk=chorelist_id)
    return render(request, 'chores/detail.html', {'chorelist': list})

def chores(request, chorelist_id):
    return HttpResponse("You're looking at Chores from ChoreList #%s" % chorelist_id)


def choredetail(request, chorelist_id, chore_id):
    return HttpResponse("You're looking at Chore #%s  from ChoreList # %s" %(chore_id, chorelist_id))

