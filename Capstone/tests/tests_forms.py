from django.test import SimpleTestCase

from Capstone.forms import usersForm

class TestFroms(SimpleTestCase):
    def test_vaild_form(self):
        form=usersForm(data={'User_Name':'revanth','Email':'revanth@gmail.com','Password':'revanth'})
        self.assertTrue(form.is_valid())
    def test_invalid_form(self):
        form=usersForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),3)
