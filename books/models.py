# -*- coding: utf-8 -*-
from django.db import models

class Genre(models.Model):
    bezeichnung = models.CharField(max_length=200)

    def __unicode__(self):
        return self.bezeichnung

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

class Autor(models.Model):
    vorname = models.CharField(max_length=200)
    nachname = models.CharField(max_length=200)

    def __unicode__(self):
        return self.vorname + " " + self.nachname

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autoren"
        
class Verlag(models.Model):
    bezeichnung = models.CharField(max_length=200)

    def __unicode__(self):
        return self.bezeichnung

    class Meta:
        verbose_name = "Verlag"
        verbose_name_plural = "Verlage"
    
class Tag(models.Model):
    bezeichnung = models.CharField(max_length=200)

    def __unicode__(self):
        return self.bezeichnung

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

class Buch(models.Model):
    """
    Diese Klasse, stellt die Hauptklasse des Systems dar.
    """
    titel = models.CharField("Buchtitel", max_length=200)
    autor = models.ManyToManyField(Autor, blank=True, null=True)
    veroeffentlichung = models.DateField("Veröffentlichung", blank=True, null=True)
    verlag = models.ForeignKey(Verlag, blank=True, null=True)
    cover = models.ImageField("Buchcover", blank=True, null=True, upload_to="/media/images/cover/")
    genre = models.ManyToManyField(Genre, blank=True, null=True)
    # ISBN besitzt unter der Annahme von ISBN-13 mit Trennzeichen eine maximale
    # Länge von 17 Zeichen
    isbn = models.CharField("ISBN", max_length=17, blank=True)
    bewertung = models.PositiveSmallIntegerField(blank=True, null=True)
    bemerkung = models.TextField(blank=True)
    tag = models.ManyToManyField(Tag, blank=True, null=True)
    preis = models.CharField(max_length=10, blank=True)
    lesezeichen = models.PositiveIntegerField("Seitennr. des Lesezeichens", blank=True, null=True)

    def __unicode__(self):
        return self.titel

    class Meta:
        verbose_name = "Buch"
        verbose_name_plural = "Bücher"
