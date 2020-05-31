from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import User
# Create your views here.


def index(request):
    request.GET.get()
    # result = User.objects.value()
    # for data in result:
    #     print("name = " + data.name)
    return HttpResponse("result")
