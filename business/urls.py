from django.contrib import admin
from django.urls import path, include
from .views import IndexView, AboutView, RecruitingView, ContactView, QuoteoView, EmailView, create_quote, ServiceView, MaisonView, OfficeView, CopView, DesView, RemView

app_name= 'business'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('service', ServiceView.as_view(), name='service'),
    path('about', AboutView.as_view(), name='about'),
    path('maison', MaisonView.as_view(), name='maison'),
    path('office', OfficeView.as_view(), name='office'),
    path('cop', CopView.as_view(), name='cop'),
    path('des', DesView.as_view(), name='des'),
    path('rem', RemView.as_view(), name='rem'),
    path('recruiting', RecruitingView.as_view(), name='recruiting'),
    path('contact', ContactView.as_view(), name='contact'),
    path('quote', QuoteoView.as_view(), name='quote'),
    path('email', EmailView.as_view(), name='email'),
    path('create_quote', create_quote, name='create_quote'),

   ]

