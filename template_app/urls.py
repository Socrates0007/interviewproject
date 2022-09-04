from django.urls import path

from .views import template_list_view,template_detail_view

urlpatterns = [
    path('',template_list_view,name='templates'),
    path('<int:pk>/',template_detail_view,name='template_detail'),

]