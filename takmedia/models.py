from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from ckeditor_uploader.fields import RichTextUploadingField
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    pass



class Communiquons_projet(models.Model):
    nom = models.CharField(max_length=100)
    courrier = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    sujet = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.nom


class Team(models.Model):
    membre = models.ForeignKey(User, on_delete=models.CASCADE)
    prenom = models.CharField(max_length=100)
    domaine = models.CharField(max_length=100)
    
    def __str__(self):
        return self.prenom

class Soumission_client(models.Model):
    nom = models.CharField(max_length=100)
    courrier = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    sujet = models.CharField(max_length=100)
    entreprise = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField()
    

    def __str__(self):
        return self.nom


class Blog(models.Model):
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    titre = models.CharField(max_length=120)

    image = models.ImageField()
    date = models.DateTimeField(default=timezone.now)
    body = RichTextUploadingField()
    slug = models.SlugField(null=False, unique=True)  # new

    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    likes = models.ManyToManyField(User, blank=True, related_name='blogpost_like')
    #dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')

    def __str__(self):
        return self.titre
