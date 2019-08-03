# pylint: disable=no-value-for-parameter
from django.test import TestCase
from .models import User


class UserRegistrationTest(TestCase):

    def test_create_user(self):
        """
        Testing create user functionality
        """

        user = User.objects.create_user(
            email='normal@testing.com',
            password='foobar',
        )
        self.assertEqual(user.email, 'normal@testing.com')
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        try:
            self.assertIsNone(user.username)
            self.assertIsNone(user.first_name)
            self.assertIsNone(user.last_name)

        except AttributeError:
            pass

        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password='foobar')

    def test_create_superuser(self):
        """
        Testing create superuser functionality
        """

        superuser = User.objects.create_superuser(
            email='normal@testing.com',
            password='foobar',
        )
        self.assertEqual(superuser.email, 'normal@testing.com')
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

        try:
            self.assertIsNone(superuser.username)
            self.assertIsNone(superuser.first_name)
            self.assertIsNone(superuser.last_name)

        except AttributeError:
            pass

        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user.com', password='foo', is_superuser=False
            )
