""" Test para el API de Cliente """
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from client.models import (
    Client
)

class ClientAPITest(TestCase):
    """ Configuracion de los campos bases """
    def setUp(self):
        self.client = APIClient()
        
        #Se crean los datos basicos para la prueba
        self.client_data = {
            "first_name": "test_name",
            "last_name": "test_last",
            "country": "test_country",
            "active": True,
        }
        
        self.client_instance = Client.objects.create(**self.client_data)
        
    """ Prueba unitaria para el metodo de crear un cliente """
    def test_create_client(self):
        response = self.client.post('/api/clients/client/', self.client_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)        
        self.assertTrue(Client.objects.filter(first_name="test_name").exists())
        self.assertTrue(Client.objects.filter(last_name="test_last").exists())
        self.assertTrue(Client.objects.filter(country="test_country").exists())

    """ Prueba unitaria para el metodo de listar todos los clientes """
    def test_get_clients(self):
        response = self.client.get('/api/clients/client/', format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    """ Prueba unitaria para el metodo de listar un cliente por su ID """
    def test_get_client(self):
        response = self.client.get(f'/api/clients/client/{self.client_instance.id}/', format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], self.client_data['first_name'])
        self.assertEqual(response.data['last_name'], self.client_data['last_name'])
        self.assertEqual(response.data['country'], self.client_data['country'])
        self.assertEqual(response.data['active'], self.client_data['active'])
        
    """ Prueba unitaria para el metodo de actualizar todo el cliente """
    def test_update_client(self):
        # Nuevos datos para actualizar el cliente
        updated_data = {
            "first_name": "usuario1",
            "last_name": "usuario11",
            "country": "Canada",
            "active": False
        }

        response = self.client.put(f'/api/clients/client/{self.client_instance.id}/', updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        
        self.client_instance.refresh_from_db()

        self.assertEqual(self.client_instance.first_name, updated_data['first_name'])
        self.assertEqual(self.client_instance.last_name, updated_data['last_name'])
        self.assertEqual(self.client_instance.country, updated_data['country'])
        self.assertEqual(self.client_instance.active, updated_data['active'])
        
    """ Prueba unitaria para el metodo de actualizar parcialmente el cliente """
    def test_partial_update_client(self):
        # Nuevos datos para actualizar el cliente
        updated_data = {
            "first_name": "usuario1",
            "active": False
        }

        response = self.client.patch(f'/api/clients/client/{self.client_instance.id}/', updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        
        self.client_instance.refresh_from_db()

        self.assertEqual(self.client_instance.first_name, updated_data['first_name'])
        self.assertEqual(self.client_instance.last_name, self.client_data['last_name'])
        self.assertEqual(self.client_instance.country, self.client_data['country'])
        self.assertEqual(self.client_instance.active, updated_data['active'])
        
    """ Prueba unitaria para el metodo de eliminar un cliente """
    def test_delete_client(self):
        response = self.client.delete(f'/api/clients/client/{self.client_instance.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Client.objects.filter(id=self.client_instance.id).exists())
        
    """ Prueba unitaria para el metodo de listar un cliente por su ID y que no exista """
    def test_get_client_not_found(self):
        response = self.client.get(f'/api/clients/client/15641561/', format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
