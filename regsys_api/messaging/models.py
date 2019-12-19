from django.db import models
from django.core.mail import EmailMultiAlternatives

from regsys_api.authsys.models import User
from django.template.loader import get_template
from django.utils import timezone

import requests

class Message(models.Model):
    nama_pengirim = models.CharField(max_length=50)
    email_pengirim = models.CharField(max_length=50)
    pesan = models.TextField(max_length=500)
    recieved_at = models.DateTimeField(auto_now_add=True)
    replied = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.nama_pengirim, self.email_pengirim)

    def send_line_notification(self):
        auth_token='JrtU8tFBrOugQLboQvaFpJdjlM5EvRIwUWaIwNwhGD5N6q1KcaouIgKd20VsJnNlQxc0RcBEf8nahzX6vJw9e51VcWA6BcQV+/F1PHNb5KVOGWxvvhM5CVyAx52RqInxmQGWQe8AToPTXLte/QUhUQdB04t89/1O/w1cDnyilFU='
        hed = {'Authorization': 'Bearer ' + auth_token}
        data = {
            "to": "C0fd8ac3ed9f41fe84d3de2d7581d52ed",
            "messages":[
                {
                    "type":"text",
                    "text":"[INFO PESAN]\n{} baru saja mengirim pesan:\n{}.".format(self.nama_pengirim,  self.pesan)
                }
            ]
        }

        url = 'https://api.line.me/v2/bot/message/push'

        requests.post(url, json=data, headers=hed)

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
            from_email='Sekretariat IFest #8 <sekret@ifest-uajy.com>',
            to=[self.email_pengirim],
            bcc=["sekret@ifest-uajy.com"]
        )

        mail.attach_alternative(mail_html_message, "text/html")
        mail.send(
            fail_silently=False
        )

