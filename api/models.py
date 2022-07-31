from django.db import models
from accounts.models import User


class Plateforme(models.Model):
    objects = models.Manager()
    plateforme = models.CharField(max_length=64, unique=True)
    plateforme_url = models.CharField(max_length=256)

    def __str__(self):
        return self.plateforme


class Anime(models.Model):
    objects = models.Manager()

    nom = models.CharField(max_length=64)
    nom_original = models.CharField(max_length=64, null=True)
    description = models.TextField(null=True)
    url = models.SlugField(null=True)
    nombres_saisons = models.IntegerField(null=True)
    status_anime = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    image = models.ImageField(upload_to="anime_image", blank=True, null=True)
    plateforme = models.ForeignKey(Plateforme, on_delete=models.CASCADE, related_name="anime")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="anime")

    def __str__(self):
        return self.nom
