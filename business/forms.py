import email
from django import forms
from django.conf import settings
from django.forms import ModelForm
from config.settings import EMAIL_HOST_USER, EMAIL_RECIPIENT
from .models import Contact, Formule, Quote, Hiring, Surface
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.translation import gettext as _
        
class ContactForm(ModelForm) :
    class Meta: 
        model = Contact 
        fields = '__all__' 
        
    def get_info(self):
        cleaned_data = super().clean()

        name = cleaned_data.get('name').strip()
        phone = cleaned_data.get('phone')
        email = cleaned_data.get('email')
        subject = cleaned_data.get('subject') 
        message = cleaned_data.get('message') 
        msg =  f'Bonjour OCRAN NADAFA,  {name}, ayant le mail: {email}, et le numero : {phone}, vous a envoyé le message suivant: {message}'
        return subject, msg, email

    def send_email(self):
        subject, msg, email = self.get_info()
        send_mail(
            subject=subject,
            message=msg,
            from_email= EMAIL_HOST_USER,
            recipient_list= EMAIL_RECIPIENT,
        )



class QuoteForm(ModelForm) :
    class Meta: 
        model = Quote 
        fields = '__all__' 
      
    def get_info(self):
            cleaned_data = super().clean()
            email = cleaned_data.get('email')
            phone = cleaned_data.get('phone')
            formule = cleaned_data.get('formule')
            bien = cleaned_data.get('bien')
            surface = cleaned_data.get('surface')
            msg =  f'Bonjour OCRAN NADAFA,  une personne ayant le mail: {email}, et le numero de telephone suivant:  {email}, a demandé un devis, avec les inforamtions suivantes, pack : {formule}, type de bien: {bien}, et la surface : {surface} .'
            return phone, msg, email

    def send_email(self):
        subject, msg, email = self.get_info()
        send_mail(
            subject=subject,
            message=msg,
            from_email= EMAIL_HOST_USER,
            recipient_list=EMAIL_RECIPIENT,
        )
    





class HiringForm(ModelForm) :
    class Meta: 
        model = Hiring 
        fields = '__all__' 
        
    def get_info(self):
            
        cleaned_data = super().clean()
        name = cleaned_data.get('name').strip()
        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')
        subject = cleaned_data.get('subject')
        msg =  f'Bonjour OCRAN NADAFA,  une personne ayant le nom: {name}, le mail: {email}, et le numero de telephone suivant:  {phone}, a remplis un formulaire de recrutement.'
        
        return subject, msg, email

    def send_email(self):

        subject, msg, email = self.get_info()

        send_mail(
            subject=subject,
             message=msg,
            from_email= EMAIL_HOST_USER,
            recipient_list=EMAIL_RECIPIENT,
            )
