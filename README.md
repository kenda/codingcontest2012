# Über
Das Projekt entstand im Rahmen des [Coding Contest](http://www.coding-contest.de/) 2012. Die verwendete Plattform ist dabei Python.

## Aufgabenstellung
	Du sollst eine Web Applikation schreiben, die zur Verwaltung von Büchern 
	dient - ganz im Sinne einer digitalen Bibliothek. Bei den Features hast 
	du freie Hand - es ist also deine Kreativität gefragt! Wer die Web Applikation
	mit einer API ausstattet, kann zusätzliche Punkte bekommen.

# Lösung
Die erstellte Webanwendung basiert auf [Django 1.4](http://djangoproject.com) und bindet weitere
Bibliotheken ein. Für den vollen Funktionsumfang sind folgende Mindest-Vorraussetzungen erforderlich:

* Python 2.5
* [Django 1.4](https://www.djangoproject.com/download/)
* python-mimeparse
* python-dateutil
* Python Imaging Library

Optional:
* [sqlite](http://www.sqlite.org/)
* [docutils](http://docutils.sourceforge.net/)

## Installation
Nachdem Django und die benötigten Bibliotheken installiert wurden kann die Anwendung mittels

`python manage.py runserver`

aus dem Projektverzeichnis gestartet werden und steht dann unter 

`http://localhost:8000`

bereit. Dem Projekt liegt eine sqlite-Datenbank mit Testdaten
bereits bei. Bei Bedarf kann aber auch eine beliebige andere Datenbank verwendet werden. Die Datenbank
besitzt bereits einen Django Administrator mit dem Namen `admin` und Passwort `admin`.

## Hinweise
Um ein einfaches Ausprobieren des Systems zu ermöglichen wird eine Einstellungsdatei mit ausgeliefert
die u.a. einen SECRETKEY preis gibt. Desweiteren liegt der Anwendung ein API-Key für das REST-Interface
bei.

## Funktionsumfang

### Backend
Das Backend besteht aus 6 Klassen, deren recht einfach gehaltene Beziehungen nachfolgendes UML-Klassendiagramm darstellt:
<img src="https://github.com/kenda/codingcontest2012/raw/master/uml_classes.png" width="800px" />

### REST-Schnittstelle
Die Buch-Verwaltung besitzt eine [REST](http://de.wikipedia.org/wiki/Representational_State_Transfer)-Schnittstelle, die es in der Standard-Konfiguration ermöglicht von außen beliebig neue Objekte anzulegen, zu ändern oder zu löschen. Die verwendete Bibliothek ist dabei [Tastypie](http://tastypieapi.org/).

Eine Beispiel-Abfrage, welche alle gespeicherten Bücher als JSON zurückgibt, sehe mittels [Curl](http://curl.haxx.se/docs/httpscripting.html) wiefolgt aus:

`curl --user admin:admin http://localhost:8000/api/v1/buch/?format=json`

Für eine volle Dokumentation über den Funktionsumfang der Schnittstelle, siehe "[interacting with the API](http://readthedocs.org/docs/django-tastypie/en/latest/interacting.html)". Die auf der Übersichtsseit angezeigten Daten werden exemplarisch über die API angefordert.
v

### Such- und Filterfunktion
Aufbauend auf [Exhibit](http://simile-widgets.org/exhibit/) lassen sich die erstellten Bücher
durchsuchen und durch umfangreiche Filterkriterien einschränken.

### Ansichten
Es werden drei Ansichten auf den Bücherbestand zur Verfügung gestellt. Eine Vorschauansicht, eine
tabellarische Darstellung und eine Zeitreihen-Ansicht basierend auf dem Veröffentlichungsdatum der
Bücher.

### Exportfunktion
In der Übersicht ist es möglich die angezeigten Bücher in unterschiedliche Formate wie RDF/XML oder 
tsv zu exportieren. Dazu muss mit dem Mauszeiger über einen Eintrag gefahren werden, worauf hin ein
orange-farbenes Scherensymbol eingeblendet wird. Dieses stellt das Exportmenü zur Verfügung.

### Administration
Um über Bücher hinausgehend für alle Klassen Instanzen zu erzeugen gibt es ein Administrations-Interface welches standardmäßig unter `/admin/` aufgerufen werden kann.

## Dokumentation
Sofern docutils installiert ist steht unter `/admin/doc/` eine Entwickler-Dokumentation zur Verfügung,
die neben den Core-Funktionen von Django auch die Dokumentation der entwickelten Klassen umfasst.

## Tests
Um die erstellten Tests auszuführen muss lediglich 

`python manage.py test books`

im Projektverzeichnis ausgeführt werden, worauf hin alle Tests ausgeführt werden.
