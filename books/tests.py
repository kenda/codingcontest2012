from django.contrib.auth.models import User
from django.test import TestCase

from tastypie.test import ResourceTestCase

from books.api.resources import AutorResource


class AutorResourceTest(ResourceTestCase):
    def setUp(self):
        super(AutorResourceTest, self).setUp()

        # Create a user.
        self.username = 'test'
        self.password = 'test'
        self.user = User.objects.create_user(self.username, 'test@example.com',
                                             self.password)

    def get_credentials(self):
        return self.create_basic(self.username, self.password)

    def test_get_unauthorized(self):
        self.assertHttpUnauthorized(self.api_client.get('/api/v1/autor/',
                                                        format='json'))

    def test_get_xml(self):
        self.assertValidXMLResponse(self.api_client.get('/api/v1/autor/',
                                                        format='xml',
                                                        authentication=self.get_credentials()))

    def test_post_unauthenticated(self):
        self.assertHttpUnauthorized(self.api_client.post('/api/v1/autor/',
                                                         format='json',
                                                         data={
                                                             "vorname": "Max",
                                                             "nachname": "Mustermann"
                                                         }))

    def test_post_list(self):
        self.assertHttpCreated(self.api_client.post('/api/v1/autor/',
                                                    format='json',
                                                    data={
                                                        "vorname": "Max",
                                                        "nachname": "Mustermann"
                                                    },
                                                    authentication=self.get_credentials()))
