from django.db import models






class Communiquons_projet(models.Model):
    nom = models.CharField(max_length=100)
    courrier = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    sujet = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.nom


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
    titre = models.CharField(max_length=100)
    image = models.ImageField()
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.titre

