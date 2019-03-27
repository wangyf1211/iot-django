from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Distance,Temp
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.
# test
def hello(request):
    return JsonResponse({'result': 200, 'msg': 'success'})


@csrf_exempt
def get_distance(request):
    if request.method == 'GET':
        data=serializers.serialize('python',Distance.objects.all())
        res={
            'success':True,
            'data':data
        }
        return HttpResponse(json.dumps(res,cls=DjangoJSONEncoder),content_type='application/json')

@csrf_exempt
def get_temp(request):
    if request.method == 'GET':
        data = serializers.serialize('python', Temp.objects.all())
        res = {
            'success': True,
            'data': data
        }
        return HttpResponse(json.dumps(res, cls=DjangoJSONEncoder), content_type='application/json')