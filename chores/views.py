from django.shortcuts import render, get_object_or_404
from  django.http import HttpResponse, Http404
from .models import ChoreList,Chore
# Create your views here.


def index(request):
    lists = ChoreList.objects.all()
    return render(request, 'chores/index.html', { 'chorelists': lists })


def detail(request, chorelist_id):

    list = get_object_or_404(ChoreList, pk=chorelist_id)

    return render(request, 'chores/detail.html', {'chorelist': list})

def chores(request, chorelist_id):
    list = get_object_or_404(Chore, pk=chorelist_id)
    return render(request, 'chores/chores.html')


def choredetail(request, chorelist_id, chore_id):
    return HttpResponse("You're looking at Chore #%s  from ChoreList # %s" %(chore_id, chorelist_id))

