from django.core.mail import EmailMessage
from schMartket.settings import EMAIL_HOST_USER


class Utils:
    @staticmethod
    def send_mail(data):
        print(EMAIL_HOST_USER)
        email = EmailMessage(
            subject=data['subject'], body=data['body'], to=[data['recipient']])
        email.send()
