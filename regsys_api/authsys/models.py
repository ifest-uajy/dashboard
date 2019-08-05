from string import (
    ascii_letters, digits
)

from django.contrib.auth.models import (
    AbstractUser, BaseUserManager
)

from django.db import models
from django.utils.crypto import get_random_string
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

def generate_email_token():
    return get_random_string(length=32, allowed_chars=ascii_letters + digits)


class UserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        """
        Create a user with given email and password
        """

        if not email:
            raise ValueError('The given email must be set')
        if not password:
            raise ValueError('The given password must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password, **extra_fields):
        """
        Create a regular user with given email and password
        This function will create a user with
        is_staff is false and is_superuser is false
        """

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        Create a superuser user with given email and password
        This function will create a user with
        is_staff is true and is_superuser is true
        """

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """
    Custom user model for regsys_api
    """

    username = None
    first_name = None
    last_name = None

    full_name = models.CharField(max_length=100)
    email = models.EmailField(_('email address'), unique=True)
    is_confirmed = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class RegistrationHandler(models.Model):
    """
    Issue a token send via email to confirm their registration
    """

    user = models.OneToOneField(
        to=User, related_name='registration_token', on_delete=models.CASCADE)
    token = models.CharField(
        max_length=32, default=generate_email_token, unique=True)
    is_confirmed = models.BooleanField(default=False)
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '%s (%s)' % (self.user.full_name, self.user.email)

    def send_email(self):
        context = {
            'user': self.user,
            'token': self.token
        }

        text_template = get_template('registration_email.txt')
        html_template = get_template('registration_email.html')

        mail_text_message = text_template.render(context)
        mail_html_message = html_template.render(context)

        mail = EmailMultiAlternatives(
            subject='Mohon Konfirmasi Alamat Email Anda',
            body=mail_text_message,
            to=[self.user.email]
        )

        mail.attach_alternative(mail_html_message, "text/html")
        mail.send()
        
        self.sent_at = timezone.now()
        self.save()


class ForgotPasswordHandler(models.Model):
    """
    Issue a token send via email to reset their password
    """

    user = models.OneToOneField(
        to=User, related_name='password_token', on_delete=models.CASCADE)
    token = models.CharField(
        max_length=32, default=generate_email_token, unique=True)
    is_confirmed = models.BooleanField(default=False)
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '%s (%s)' % (self.user.full_name, self.user.email)

    def send_email(self):

        self.sent_at = timezone.now()
        self.save()