from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.choose, name='choose'),
    path('template4',views.cse_template_4,name='cse_template_4'),
    
    path('<str:style>',views.generate,name ='generate'),
]