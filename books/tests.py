# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.test import TestCase

from tastypie.test import ResourceTestCase

from books.api.resources import AutorResource


class AutorResourceTest(ResourceTestCase):
    """
    Testklasse zum Testen der REST-Schnittstelle für Autor-Ressourcen.
    """
    def setUp(self):
        super(AutorResourceTest, self).setUp()

        # Test-User anlegen
        self.username = 'test'
        self.password = 'test'
        self.user = User.objects.create_user(self.username, 'test@example.com',
                                             self.password)

    def get_credentials(self):
        """ Methode zum Authentifizieren an der Schnittstelle. """
        return self.create_basic(self.username, self.password)

    def test_get_unauthorized(self):
        """ Test ob Authentifizierung via GET funktioniert. """
        self.assertHttpUnauthorized(self.api_client.get('/api/v1/autor/',
                                                        format='json'))

    def test_get_xml(self):
        """ Test ob XML-Rückgabe funktioniert. """
        self.assertValidXMLResponse(self.api_client.get('/api/v1/autor/',
                                                        format='xml',
                                                        authentication=self.get_credentials()))

    def test_post_unauthenticated(self):
        """ Test ob Authentifizierung via POST funktioniert. """
        self.assertHttpUnauthorized(self.api_client.post('/api/v1/autor/',
                                                         format='json',
                                                         data={
                                                             "vorname": "Max",
                                                             "nachname": "Mustermann"
                                                         }))
