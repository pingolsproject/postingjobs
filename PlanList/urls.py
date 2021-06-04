from django.conf.urls import url
from RPList import views 

urlpatterns = [    
    url(r'^$', views.home_page, name='home_page'),    
    url(r'^RPList/new$', views.new_list, name='new_list'),    
    url(r'^RPList/(\d+)/$', views.view_list, name='view_item'),    
    url(r'^RPList/(\d+)/add_item$', views.add_item, name='add_item'),]