from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("You're at the ChoreList index")


def detail(request, chorelist_id):
    return HttpResponse("You're looking at Chore list #%s" % chorelist_id)


def chores(request, chorelist_id):
    return HttpResponse("You're looking at Chores from ChoreList #%s" % chorelist_id)


def choredetail(request, chorelist_id, chore_id):
    return HttpResponse("You're looking at Chore #%s  from ChoreList # %s" %(chore_id, chorelist_id))

