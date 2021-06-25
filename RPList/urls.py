from django.conf.urls import url , include
from django.contrib import admin
from django.urls import path
from RPList import views 

urlpatterns = [    
    url(r'^$', views.home_page, name='home_page'),         
    url('job1/', views.job1, name='job1'),    
    url('job2/', views.job2, name='job2'),
    url('job3/', views.job3, name='job3'),
    url('job4/', views.job4, name='job4'),
    
    url('about/', views.about, name='about'), 



    ]