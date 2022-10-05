from django.contrib import admin
from django.urls import path,include
from . import  views
from .views import Another,BookViewset

from rest_framework import routers
router=routers.DefaultRouter()
router.register('books',BookViewset)

urlpatterns = [
    path('',views.first),
    path('rest',include(router.urls)),
    path('another',Another.as_view())
]
