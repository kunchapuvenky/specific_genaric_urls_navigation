from django.urls import path
from app1.views import *

app_name='sree'

urlpatterns=[
    path('lohi/',lohi,name='lohi'),
]