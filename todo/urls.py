from django.urls import path,include
from . import views
urlpatterns=[
    path('add/',views.MyaddPage,name='MyaddPage'),
    path('viewall/',views.My_details,name='My_details'),
]