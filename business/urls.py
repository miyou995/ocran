from django.contrib import admin
from django.urls import path, include
from .views import IndexView, AboutView, RecruitingView, ContactView, QuoteoView,  ServiceView, ServiceDetail
# create_quote
app_name= 'business'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('service', ServiceView.as_view(), name='service'),
    path('about', AboutView.as_view(), name='about'),
    path('service_detail/<slug:slug>/', ServiceDetail.as_view(), name='service_detail'),

    path('recruiting', RecruitingView.as_view(), name='recruiting'),
    path('contact', ContactView.as_view(), name='contact'),
    path('quote', QuoteoView.as_view(), name='quote'),
    # path('create_quote', create_quote, name='create_quote'), 

   ]

