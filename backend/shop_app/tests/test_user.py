from rest_framework.test import APITestCase
from django.urls import reverse
from ..models import User


class RegisterTests(APITestCase):
    def setUp(self):
        self.email = 'testuser@email.com'
        self.password = 'Pass*32word4'
        self.url = 'shop_app:register'

    def test_register(self):
        data = self.client.post(reverse(self.url), data={
            'email': self.email,
            'password': self.password,
            'password2': self.password,

        })

        self.assertEqual(data.status_code, 201)
        users = User.objects.all()
        self.assertEqual(users.count(), 1)

    def test_email_validation_register(self):
        data = self.client.post(reverse(self.url), data={
            'email': 'pass',
            'password': self.password,
            'password2': self.password,

        })

        self.assertEqual(data.status_code, 400)

    def test_password_validation_register(self):
        data = self.client.post(reverse(self.url), data={
            'email': self.email,
            'password': 'pass',
            'password2': 'pass',

        })

        self.assertEqual(data.status_code, 400)

