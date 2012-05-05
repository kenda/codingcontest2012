# -*- coding: utf-8 -*-
from django.db import models


class Genre(models.Model):
    """
    Ein Genre umfasst eine bestimmte Kategorie eines Buches.
    Bspw. "Krimi", "Biografie" oä.
    Denkbar ein umfassenderes Genre-Modell als Taxonomie zu
    implementieren.
    """
    bezeichnung = models.CharField(max_length=200)

    def __unicode__(self):
        return self.bezeichnung

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"


class Autor(models.Model):
    """
    Die Klasse Autor beschreibt genau eine Person,
    die als Autor auftritt.
    Weitere biografische Fakten denkbar und leicht
    erweiterbar.
    """
    vorname = models.CharField(max_length=200)
    nachname = models.CharField(max_length=200)

    def __unicode__(self):
        return self.vorname + " " + self.nachname

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autoren"


class Verlag(models.Model):
    """
    Die als Verleger auftretende Firma.
    """
    bezeichnung = models.CharField(max_length=200)

    def __unicode__(self):
        return self.bezeichnung

    class Meta:
        verbose_name = "Verlag"
        verbose_name_plural = "Verlage"


class Tag(models.Model):
    """
    Ein Tag beschreibt eine weitere Klassifikations-
    Eigenschaft eines Buches.
    Im Gegensatz zum Genre bspw. beschreiben beliebig
    viele Tags ein bestimmtes Objekt näher.
    """
    bezeichnung = models.CharField(max_length=200)

    def __unicode__(self):
        return self.bezeichnung

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Sammlung(models.Model):
    """
    Eine Sammlung umfasst mehrere Bücher und gruppiert
    diese so.
    Eine besondere Sammlung ist die ID 1, die "Wunschliste".
    """
    bezeichnung = models.CharField(max_length=200)

    def __unicode__(self):
        return self.bezeichnung

    class Meta:
        verbose_name = "Sammlung"
        verbose_name_plural = "Sammlungen"


class Buch(models.Model):
    """
    Diese Klasse, stellt die Hauptklasse des Systems dar.
    Ein Buch muss dabei zwingend lediglich einen Titel besitzen.
    Autor, Verlag etc. sind optional.
    """
    titel = models.CharField("Buchtitel", max_length=200)
    autor = models.ManyToManyField(Autor, blank=True, null=True)
    veroeffentlichung = models.DateField("Veröffentlichung", blank=True,
                                         null=True)
    verlag = models.ForeignKey(Verlag, blank=True, null=True)
    cover = models.ImageField("Buchcover", blank=True, null=True,
                              upload_to="images/cover/",
                              default="images/cover/blank.png")
    genre = models.ManyToManyField(Genre, blank=True, null=True)
    sammlung = models.ForeignKey(Sammlung, blank=True, null=True)
    # ISBN besitzt unter der Annahme von ISBN-13 mit Trennzeichen eine maximale
    # Länge von 17 Zeichen
    isbn = models.CharField("ISBN", max_length=17, blank=True)
    # Eine Bewertung auf einer posititiven Skala, je höher die Bewertung, desto
    # besser die Einschätzung des Benutzers
    bewertung = models.PositiveSmallIntegerField(blank=True, null=True)
    bemerkung = models.TextField(blank=True)
    tag = models.ManyToManyField(Tag, blank=True, null=True)
    preis = models.CharField(max_length=10, blank=True)
    # Zum sicheren Ablegen von Lesezeichen kann pro Buch eine Seitenzahl
    # als aktuelles Lesezeichen angelegt werden
    lesezeichen = models.PositiveIntegerField("Seitennr. des Lesezeichens",
                                              blank=True, null=True)

    def __unicode__(self):
        return self.titel

    class Meta:
        verbose_name = "Buch"
        verbose_name_plural = "Bücher"
