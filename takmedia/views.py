from django.shortcuts import render, redirect
from .forms import *







def index(request):
    soumi = Soumission_clienForm()
    if request.method == 'POST':
        soumi = Soumission_clienForm(request.POST)
        if soumi.is_valid():
            soumi.save()
            return redirect('success')
    return render(request, 'takmedia/index.html')


def apropos(request):
    return render(request, 'takmedia/about.html')

def projet(request):
    return render(request, 'takmedia/projet.html')

def contact(request):
    return render(request, 'takmedia/contact.html')


def team(request):
    return render(request, 'takmedia/team.html')


def service(request):
    return render(request, 'takmedia/service.html')

def conception(request):
    return render(request, 'takmedia/conception_site.html')



def design(request):
    return render(request, 'takmedia/design-web.html')



def boutique(request):
    return render(request, 'takmedia/boutique-en-ligne.html')

def applicationweb(request):
    return render(request, 'takmedia/application-web.html')

def referencement(request):
    return render(request, 'takmedia/referencement.html')

def monetisation_adds(request):
    return render(request, 'takmedia/monetisation.html')

def notre_expertise(request):
    return render(request, 'takmedia/expertise.html')


def clients(request):
    return render(request, 'takmedia/clients.html')


def technologie_utilise(request):
    return render(request, 'takmedia/techonologie_utiliser.html')


def soumission(request):
    communi = Communiquons_projetForm()
    if request.method == 'POST':
        communi = Communiquons_projetForm(request.POST)
        if communi.is_valid():
            communi.save()
            return redirect('success')
    return render(request, 'takmedia/soumission.html')

def Analyse_performance(request):
    return render(request, 'takmedia/analyse_performance.html')

def digital_social(request):
    return render(request, 'takmedia/digital_social.html')


def success_page(request):
    return render(request, 'takmedia/success.html')


def blog(request):
    blog_post = Blog.objects.all()
    return render(request, 'takmedia/blog.html', {'blog_post':blog_post})






