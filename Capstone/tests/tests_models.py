from django.test import TestCase
from Capstone.models import users


class Testmodels(TestCase):
    def setup(self, User_Name='revanth', Email="revanth@gmail.com", Password='revanth', ):
        return users.objects.create(

            User_Name=User_Name,
            Email=Email,

            Password=Password
        )

    def test_users(self):
        u = self.setup()
        self.assertTrue(isinstance(u, users))
        self.assertEqual(u.__str__(), u.User_Name)

