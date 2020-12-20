from django.test import SimpleTestCase
from django.urls import resolve,reverse
from Capstone.views import signup,login,home
class Testurls(SimpleTestCase):
    def test_url_resolve_home(self):
        url=reverse('home')
        self.assertEquals(resolve(url).func,home)
    def test_url_resolve_login(self):
        url=reverse('login')
        self.assertEquals(resolve(url).func,login)
    def test_url_resolve_signup(self):
        url=reverse('signup')
        self.assertEquals(resolve(url).func,signup)