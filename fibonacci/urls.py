"""
fibonacci URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from fibonacci.fiboapi import views
from rest_framework_swagger.views import get_swagger_view
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'fibo', views.FiboSeqView, basename='fibo')

swag_view = get_swagger_view(title='Sequence API',)
urlpatterns = [
    #path('admin/', admin.site.urls), #no admin required atm
    path('', include(router.urls)),
    path('swagger/', swag_view),
]
