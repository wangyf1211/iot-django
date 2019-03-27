from django.urls import path
from . import views

urlpatterns = {
    path('hello', views.hello, name='hello'),
    path('getDistance', views.get_distance, name='getDistance'),
    path('getTemp', views.get_temp, name='getTemp')
}
