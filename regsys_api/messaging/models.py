from django.db import models
from django.core.mail import EmailMultiAlternatives

from regsys_api.authsys.models import User
from django.template.loader import get_template
from django.utils import timezone

class Message(models.Model):
    nama_pengirim = models.CharField(max_length=50)
    email_pengirim = models.CharField(max_length=50)
    pesan = models.TextField(max_length=500)
    recieved_at = models.DateTimeField(auto_now_add=True)
    replied = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.nama_pengirim, self.email_pengirim)


    def send_email(self):
        context = {
            'user': self.nama_pengirim,
            'pesan': self.pesan + "\n"
        }

        text_template = get_template('email.html')
        html_template = get_template('email.html')

        mail_text_message = text_template.render(context)
        mail_html_message = html_template.render(context)

        mail = EmailMultiAlternatives(
            subject='Pesan kamu sudah kami terima',
            body=mail_text_message,
            to=[self.email_pengirim]
        )

        mail.attach_alternative(mail_html_message, "text/html")
        mail.send(
            fail_silently=False
        )

