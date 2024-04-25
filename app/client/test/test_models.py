from django.test import TestCase
from django.utils import timezone
from client.models import (
    Client
)

class ModelTests(TestCase):
    def test_client_create(self):
        client = Client.objects.create(
            first_name='javier',
            last_name='Llinares',
            country='Venezuela',
            active=True,
            creation_date=timezone.now()
        )

        # Verificacion de las propiedades
        self.assertEqual(client.first_name, 'javier')
        self.assertEqual(client.last_name, 'Llinares')
        self.assertEqual(client.country, 'Venezuela')
        self.assertTrue(client.active)
        self.assertIsNotNone(client.creation_date)