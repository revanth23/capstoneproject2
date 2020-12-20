from django.urls import reverse
from Capstone.models import users
import json
from django.test import TestCase, Client
from django.contrib.auth.models import User


class Testview(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('revanth', 'revanth@gmail.com', 'revanth')
        self.response = self.client.login(username='revanth', password='revanth')

    def test_signup_get(self):
        client = Client()
        response = client.get(reverse('signup'))
        self.assertTemplateUsed(response, "signup.html")

    def test_login_get(self):
        self.response = self.client.get(reverse('login'))
        self.assertTemplateUsed(self.response, "login.html")
        self.assertEqual(self.response.status_code, 200)

    def test_home_get(self):
        self.response = self.client.get(reverse('home'))
        self.assertTemplateUsed(self.response, "home.html")
        self.assertEqual(self.response.status_code, 200)
