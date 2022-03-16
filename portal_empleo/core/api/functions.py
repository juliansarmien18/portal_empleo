from django.core.mail.message import EmailMultiAlternatives
from django.template.loader import render_to_string
from portal_empleo.settings import EMAIL_HOST_USER as sender


def email_function(subject, body, receivers, carbon_copy, blind_carbon_copy):
    #Envio de correos
    email_message = EmailMultiAlternatives(
            subject=subject,
            body=render_to_string("email-template.html", {
                'body': body
            }),
            from_email=sender,
            to=receivers,
            cc=carbon_copy,
            bcc=blind_carbon_copy)
    email_message.content_subtype = "html"
    email_message.send()
    