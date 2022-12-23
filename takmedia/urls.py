from django.urls import path

from .import views

urlpatterns = [
    path('', views.index,name='index'),
    path('apropos/', views.apropos, name='about'),
    path('contact/', views.contact, name='contact'),
    path('conception-de-site-web/', views.conception, name='conception-site-web'),
    path('boutique-en-ligne-commerce-electronique/', views.boutique, name='boutique-en-ligne'),
    path('design-web/', views.design, name='design-web'),
    path('positionnement-moteurs-de-recherche-seo/', views.referencement, name='referencement'),
    path('application-web/', views.applicationweb, name='application-web'),
    path('referencement-payant-adwords-sem/', views.monetisation_adds, name='addsent'),
    path('notre-expertise/', views.notre_expertise, name='expertise'),
    path('clients/', views.clients, name='clients'),
    path('programmation-integration/', views.technologie_utilise, name='programmation-integration'),
    path('soumission/', views.soumission, name='soumission'),
    path('analyse-performances-web-google-analytics/', views.Analyse_performance, name='analyse-web'),
    path('digital-social/', views.digital_social, name='digital-social'),
    path('success/', views.success_page, name='success'),











    

    


]