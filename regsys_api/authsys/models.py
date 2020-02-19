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
from django.utils.timezone import utc
import datetime


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
    nomor_id = models.CharField(max_length=50)
    tanggal_lahir = models.DateField(default=None, null=True)
    is_confirmed = models.BooleanField(default=False)

    """
    Field ini untuk kebutuhan kosumsi
    """
    is_vege = models.BooleanField(default=False)
    alergic = models.CharField(max_length=120)

    """
    Field ini untuk kebutuhan legalitas peserta
    """
    is_buktiUploaded = models.BooleanField(default=False)

    """
    Field ini untuk kontak peserta
    """
    id_line = models.CharField(max_length=30)
    nomor_telepon = models.CharField(max_length=20)

    """
    Field upload KTM
    """
    #link_file = models.UUIDField(default=None)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return '%s (%s)' % (self.full_name, self.email)

    @property
    def isProfileComplete(self):
        if(not self.nomor_id or not self.tanggal_lahir or not self.nomor_telepon):
            return False
        else:
            return True

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
            'action_url': 'https://dashboard.ifest-uajy.com/confirm/' + self.token
        }

        text_template = get_template('regis_email.html')
        html_template = get_template('regis_email.html')

        mail_text_message = text_template.render(context)
        mail_html_message = html_template.render(context)

        mail = EmailMultiAlternatives(
            subject='Konfirmasi Email Akun Informatics Festival (IFest) #8',
            body=mail_text_message,
            to=[self.user.email]
        )

        mail.attach_alternative(mail_html_message, "text/html")
        mail.send(
            fail_silently=False
        )

        self.sent_at = timezone.now()
        self.save()


class ForgotPasswordHandler(models.Model):
    """
    Issue a token send via email to reset their password
    """

    user = models.OneToOneField(
        to=User, related_name='password_token', on_delete=models.CASCADE)
    browser = models.CharField(
        max_length=100
    )
    operating_system = models.CharField(
        max_length=100
    )
    token = models.CharField(
        max_length=32, default=generate_email_token, unique=True)
    is_confirmed = models.BooleanField(default=False)
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '%s (%s)' % (self.user.full_name, self.user.email)

    @property
    def get_time_diff(self):
        if self.sent_at:
            now = datetime.datetime.utcnow().replace(tzinfo=utc)
            timediff = now - self.sent_at
            return int(timediff.total_seconds())

    def send_email(self):
        context = {
            'name': self.user.full_name,
            'action_url': 'https://dashboard.ifest-uajy.com/reset-password/' + self.token,
            'operating_system': self.operating_system,
            'browser_name': self.browser
        }

        text_template = get_template('reset_pass.html')
        html_template = get_template('reset_pass.html')

        mail_text_message = text_template.render(context)
        mail_html_message = html_template.render(context)

        mail = EmailMultiAlternatives(
            subject='Reset Password Akun Informatics Festival #8',
            body=mail_text_message,
            to=[self.user.email]
        )

        mail.attach_alternative(mail_html_message, "text/html")
        mail.send()

        self.sent_at = timezone.now()
        self.save()
