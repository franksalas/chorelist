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




def choredetail(request, chorelist_id, chore_id):
    list = get_object_or_404(ChoreList, pk= chorelist_id)
    chore = get_object_or_404(Chore, pk=chore_id)
    return render(request, 'chores/choredetail.html', {'chorelist': list, 'chore': chore})


