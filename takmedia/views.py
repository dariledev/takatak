from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .forms import *
from .models import *
from django.http import HttpResponse, JsonResponse
from django.views.generic import View

from .utils import render_to_pdf #created in step 
from django.utils import timezone
from django.contrib.auth import authenticate, login
from hitcount.views import HitCountDetailView





def index(request):
    soumi = Soumission_clienForm()
    if request.method == 'POST':
        soumi = Soumission_clienForm(request.POST)
        if soumi.is_valid():
            soumi.save()
            return redirect('success')
    return render(request, 'takmedia/index.html')


def register(request):
    regis = RegisterUserForm()
    if request.method == 'POST':
        regis = RegisterUserForm(request.POST)
        if regis.is_valid():
            regis.save()
            return redirect('login')

    return render(request, 'takmedia/register.html',{'regis':regis})



def loginuser(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('index')
    return render(request, 'takmedia/login.html')



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



def formulaire_blog(request):
    form_blog = BlogForm()
    if request.method =='POST':
        form_blog = BlogForm(request.POST, request.FILES)
        if form_blog.is_valid():
            fb = form_blog.save(commit=False)
            fb.auteur = request.user
            #fb.date = request.user
            fb.save()
            return redirect('blog')
    return render(request, 'takmedia/form_blog.html', {'form_blog':form_blog})




def blog(request):
    blog_post = Blog.objects.all()
    #post = Post.objects.all()

    return render(request, 'takmedia/blog.html', {'blog_post':blog_post})




class PostDetailView(HitCountDetailView):
    model = Blog
    template_name = 'takmedia/blog_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    # set to True to count the hit
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context.update({
        'popular_posts': Blog.objects.order_by('hit_count_generic__hits'),
        })
        return context






class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {
             'today': timezone.now(), 
             'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('takmedia/commande.html', data)
        return HttpResponse(pdf, content_type='application/pdf')




