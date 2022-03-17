from django.core.mail import send_mail
from django.shortcuts import render


def register_mail(user_mail):
    
    return send_mail('Registro Exitoso', 'Usted se ha registrado existosamente en el portal de empleos','noreply@admin.com',[user_mail],fail_silently=False)
    

