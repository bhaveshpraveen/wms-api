from django.test import TestCase
from .models import Reading
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User



class ModelTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="geek")
        self.sample_pressure = 24
        self.sample_temperature = 30
        self.sample_humidity = 90
        self.readings = Reading(temperature=self.sample_temperature, pressure=self.sample_pressure, humidity=self.sample_humidity, owner=self.user)


    def test_model_can_create_a_reading(self):
        old_count = Reading.objects.all()
        self.readings.save()
        new_count = Reading.objects.all()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="geek")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.reading_data = {'temperature': 40, 'pressure': 32, 'humidity': 77, 'owner': self.user.id}
        self.response = self.client.post(
            reverse('create'),
            self.reading_data,
            format='json'
        )

    def test_api_can_post_a_reading(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


    def test_authorization_is_enforced(self):
        new_client = APIClient()
        response1 = new_client.post(
            reverse('create'),
            self.reading_data,
            format='json'
        )
        response2 = new_client.get(
            reverse('details', kwargs={'pk': Reading.object.get().id}),
            format='json'
        )
        self.assertEqual(response1.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response2.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_api_can_get_a_reading(self):
        reading = Reading.objects.get()
        response = self.client.get(
            reverse('details',  kwargs={'pk': reading.id}),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_update_a_reading(self):
        reading = Reading.objects.get()
        change_reading = {'temperature': 40, 'pressure': 160, 'humidity': 74}
        response = self.client.put(
            reverse('details', kwargs={'pk': reading.id}),
            change_reading,
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_a_reading(self):
        reading = Reading.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': reading.id}),
            format='json',
            follow=True
        )

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)


