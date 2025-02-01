"""
URL configuration for _project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from myapp.views import index_page
# from myapp.views import time_page
# from myapp.views import time_page_2
# from myapp.views import url_paths
# from myapp.views import my_math
# from myapp.views import test_template
# from myapp.views import calculator
# #from myapp.views import login
# from myapp.views import my_page
# from myapp.views import article
# from myapp.views import pages
#from django.contrib import views
from myapp import views


urlpatterns = [
   
    path('', views.index_page),
    path('time/', views.time_page),
    path('time2/', views.time_page_2),
    path('url-paths/', views.url_paths),
    path('my-math/', views.my_math),
    path('test-template/', views.test_template),
    path('calculator/', views.calculator),
    #path('login/', views.login),
    path('jmeno/<str:name>/', views.my_page),
    path('article/<slug:slug>-<int:number>/', views.article),
    path('clanky/<slug:slug>-<slug:slug1>-<slug:slug2>/', views.pages),
    path('age/', views.age_view),
    
]
