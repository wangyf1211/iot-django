from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
# test
def hello(request):
    return JsonResponse({'result': 200, 'msg': 'success'})
