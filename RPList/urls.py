from django.conf.urls import url, include
from RPList import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),   
    #url(r'companyinformations/',views.companyinformations, name='companyinformations'),
    #url(r'jobinformations/',views.jobinformations, name='jobinformations'),
    #url(r'jobrequirementss/',views.jobrequirementss, name='jobrequirementss'),
    #url(r'jobinformations/',views.jobstatus, name='jobstatus'),
    url(r'^about/$',views.about, name='about'),
    url(r'^jobinformations/$',views.jobinformations, name='jobinformations'),
    url(r'^jobrequirementss/$',views.jobrequirementss, name='jobrequirentss'),
    url(r'^jobstatus/$',views.jobstatus, name='jobstatus'),


    url(r'^new$', views.new_item, name='new_item'),
    url(r'^(\d+)/view_list$', views.view_list, name='view_list'),
    url(r'^(\d+)/add_item$', views.add_item, name='add_item'),





    url(r'edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^edit/update/(?P<id>\d+)$', views.update, name = 'update'),


    url(r'^delete/(?P<id>\d+)$', views.delete, name = 'delete'),
    ]







'''
    #url(r'^RPList/new$_Company$', views.companyinformations, name='companyinformations'),  
    #url(r'^RPList/(\d+)/$', views.jobinformations, name='jobinformations'), 
    #url(r'^RPList/(\d+)/$', views.jobrequirements, name='jobrequirementss'),    
    #url(r'^RPList/(\d+)/add_item$', views.jobstatus, name='jobstatus'),
    #url(r'^RPList/(\d+)/$', views.about, name='about'), 
    #rl(r'^RPList/(\d+)/add_item$', views.add_item, name='add_item'),
    #rl(r'^RPList/(\d+)/add_item$', views.create_list, name='create_list'),




<form method="POST" action="/new_Company">
<tr> {% for Company in companys %}          
                <td> <a href=RPList/{{Compny.id}}>{{Compny.bID}}</a></td>
                <td>{{Ccompanyname .Compny}}</td>
                <td>{{Aaddress.Addres}}</td>
                </tr> {% endfor %}
<form method="POST" action="/{{ Compny.id }}/add_info">
{% for bresidents in ibrgy.bresidents_set.all %}
        <tr>
              <{{ forloop.counter }}:  -->
              <td>{{ forloop.counter }} : {{Bbackground.bground }}</td>
              <td>{{ Ccapabilities.capa }}</td>
              <td>{{ Accreditations.accr }}</td>
              <td>{{ Accreditations.accr }}</td>
              </tr> {% endfor %} </table







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
    
    url('about/', views.about, name='about'), ]
'''