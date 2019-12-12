# pylint: disable=no-value-for-parameter
from django.test import TestCase
from .models import User, RegistrationHandler, ForgotPasswordHandler


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


class RegistrationHandlerTest(TestCase):

    def test_token_different(self):
        """
        Confirmation token should be different for each user
        """
        self.user1 = User.objects.create_user(
            email='normal@testing.com', password='foo')
        self.user2 = User.objects.create_user(
            email='normal2@testing.com', password='foo')

        attempt1 = RegistrationHandler.objects.create(user=self.user1)
        attempt2 = RegistrationHandler.objects.create(user=self.user2)

        self.assertIsNotNone(attempt1.token)
        self.assertIsNotNone(attempt2.token)
        self.assertNotEqual(attempt1.token, attempt2.token)


class ForgotPasswordHandlerTest(TestCase):

    def test_token_different(self):
        """
        Confirmation token should be different for each user
        """
        self.user1 = User.objects.create_user(
            email='normal@testing.com', password='foo')
        self.user2 = User.objects.create_user(
            email='normal2@testing.com', password='foo')

        attempt1 = ForgotPasswordHandler.objects.create(user=self.user1)
        attempt2 = ForgotPasswordHandler.objects.create(user=self.user2)

        self.assertIsNotNone(attempt1.token)
        self.assertIsNotNone(attempt2.token)
        self.assertNotEqual(attempt1.token, attempt2.token)
