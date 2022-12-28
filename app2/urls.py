from django.urls import path
from app2.views import *
app_name='shambhavi'
urlpatterns=[
    path('shambhavi/',shambhavi,name='shambhavi'),
]