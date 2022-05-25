from django.db import models
from django.urls import reverse
from tinymce import models as tinymce_models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
# Create your models here.


CHOICES = (
    ('S1' ,'70 - 200'),
    ('S2' ,'201 - 400'),
    ('S3' ,'401 - 600'),
    ('S4' ,'601 - 1000'),
  
)



class Contact(models.Model):
    name    = models.CharField(max_length=150, verbose_name='Nom')
    email   = models.EmailField(verbose_name="E-mail" )
    phone   = models.CharField(verbose_name="Téléphone" , max_length=25)
    subject = models.CharField(max_length=150, verbose_name='sujet')
    message = models.TextField(null=True, blank=True)
    class Meta:
        verbose_name = _("contact")
        verbose_name_plural = _("contacts")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("business:contact", kwargs={"pk": self.pk})

 
   
class Hiring(models.Model):
    name        = models.CharField(max_length=150, verbose_name='Nom')
    email       = models.EmailField(verbose_name="E-mail", null=True, blank=True)
    phone       = models.CharField(verbose_name="Téléphone" , max_length=25)
    birth_date  = models.DateField() 
    birth_place = models.CharField(max_length=150, verbose_name='lieu de naissance', null=True, blank=True)
    message     = models.TextField(verbose_name='experience', null=True, blank=True)
    cv_file     = models.FileField(upload_to='media', verbose_name='CV', null=True, blank=True)

    class Meta:
        verbose_name = _("hiring")
        verbose_name_plural = _("hirings")
    
    def __str__(self):
        return str(self.email)
  

    def get_absolute_url(self):
        return reverse("business:hiring", kwargs={"pk": self.pk})




class Formule(models.Model):
    formule        = models.CharField(verbose_name="Pack nettoyage",max_length=150, )
    porte          = models.IntegerField(verbose_name="nombre de fenetre", null=True, blank=True)
    price          = models.IntegerField(verbose_name="prix", default=0)
    description     = models.TextField(verbose_name='Descriptions du pack', null=True, blank=True)
    class Meta:
        verbose_name = _("formule")
        verbose_name_plural = _("formules")

    def __str__(self):
        return self.formule

    def get_absolute_url(self):
        return reverse("business:quote", kwargs={"pk": self.pk})
 
    
class Bien(models.Model):
    name         = models.CharField(verbose_name="type de bien" , max_length=25)
    price        = models.IntegerField(verbose_name="prix", default=0)
    
    class Meta:
        verbose_name = _("bien")
        verbose_name_plural = _("biens")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("business:quote", kwargs={"pk": self.pk})  
    



class Surface(models.Model):
    surface                = models.CharField(choices=CHOICES,verbose_name="surface en m2", max_length=2)
    price                  = models.IntegerField(verbose_name="prix", default=0)
    class Meta:
        verbose_name = _("surface")
        verbose_name_plural = _("surfaces")

    def __str__(self):
        return self.surface

    def get_absolute_url(self):  
        return reverse("business:quote", kwargs={"pk": self.pk})  
    
    
class Quote(models.Model):
    email       = models.EmailField(verbose_name="E-mail")
    phone       = models.CharField(verbose_name="Téléphone" , max_length=25) 
    formule     = models.ForeignKey(Formule, blank=True, null=True, on_delete=models.CASCADE) 
    bien        = models.ForeignKey(Bien, blank=True, null=True, on_delete=models.CASCADE) 
    surface     = models.ForeignKey(Surface, blank=True, null=True, on_delete=models.CASCADE) 

    class Meta:
        verbose_name = _("quote")
        verbose_name_plural = _("quotes")

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("business:quote", kwargs={"pk": self.pk})
    
    def get_total_cost(self):
        return self.surface.price +  self.bien.price + self.formule.price


class Business(models.Model):
    name            = models.CharField(verbose_name="Nom de l'entreprise", max_length=100)
    logo            = models.ImageField(upload_to='images/logos', verbose_name='Logo')
    favicon         = models.ImageField(upload_to='images/logos', verbose_name="Favicon", blank=True, null=True)
    logo_negatif    = models.ImageField(upload_to='images/slides', verbose_name="Logo négatif", blank=True, null=True)
    title           = models.CharField(verbose_name="Titre", max_length=50, blank=True)
    adress          = models.CharField(verbose_name="Adresse", max_length=50, blank=True)
    email           = models.EmailField(verbose_name="email de l'entreprise", max_length=50, blank=True)
    email2          = models.EmailField(verbose_name="2eme email de l'entreprise", max_length=50, blank=True)
    email3          = models.EmailField(verbose_name="email de receptions, contact, devis, recrutement", max_length=50, blank=True)
    phone           = models.CharField(verbose_name="numéro de téléphone de l'entreprise", max_length=50, blank=True)
    phone2          = models.CharField(verbose_name="2eme numéro de téléphone de l'entreprise", max_length=50, null=True,blank=True)
    phone3          = models.CharField(verbose_name="3eme numéro de téléphone de l'entreprise", max_length=50, null=True,blank=True)
    about           = tinymce_models.HTMLField(verbose_name='Text a propos', blank=True, null=True)
    about_2          = tinymce_models.HTMLField(verbose_name="Page d'accueil", blank=True, null=True)
    about_photo2     = models.ImageField(verbose_name="Photo a propos Page d'accueil ", upload_to='images/slides', blank=True, null=True)
    mini_about      = models.TextField(verbose_name="Petit texte a propos de l'entreprise ( bas de page)", blank=True, null=True)
    about_photo     = models.ImageField(verbose_name="Photo a propos ", upload_to='images/slides', blank=True, null=True)
    facebook        = models.URLField(verbose_name="Lien page Facebook", max_length=300, blank=True, null=True)
    insta           = models.URLField(verbose_name="Lien page Instagram", max_length=300, blank=True, null=True)
    linkedin        = models.URLField(verbose_name="Lien page LinkedIn", max_length=300, blank=True, null=True)

    
    def __str__(self):
        return self.name
    def image_tag(self):
        return format_html('<img src="{}" height="150"  />'.format(self.logo.url))
    image_tag.allow_tags = True
    class Meta:
        verbose_name = ' Infomation'
        verbose_name_plural = ' Infomations'

    def clean(self):
        model = self.__class__
        if (model.objects.count() > 0 and
                self.id != model.objects.get().id):
            raise ValidationError("Vous ne pouvez pas rajouter d'entreprise")

    def get_recipient(self):
        return self.email3

class ActiveManager(models.Manager):
    def active(self):
        return self.filter(active=True)

class Slide(models.Model):
    photo      = models.ImageField(verbose_name="Slide haut de page", upload_to='slides/' )
    actif  = models.BooleanField(verbose_name='actif', default=True)
    objects = ActiveManager()

    class Meta:
        verbose_name = 'slide'
        verbose_name_plural = 'slides'
    
  
    def clean(self):
        model = self.__class__
        if (model.objects.count() > 0 and
                self.id != model.objects.get().id):
            raise ValidationError("Vous ne pouvez pas rajouter d'autres Slides")



class About(models.Model):
    name            = models.CharField(verbose_name="Nom de l'entreprise", max_length=100,  blank=True, null=True)
    image_high      = models.ImageField(upload_to='images/', verbose_name='image_1', blank=True, null=True)
    image_low       = models.ImageField(upload_to='images/', verbose_name="image_2", blank=True, null=True)
    title           = models.CharField(verbose_name="Titre", max_length=50, blank=True) 
    about_high      = tinymce_models.HTMLField(verbose_name='Text a propos', blank=True, null=True)
    about_low       = tinymce_models.HTMLField(verbose_name='Page a propos 2', blank=True, null=True)
 
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'abouts'


class Service(models.Model):
    name            = models.CharField(verbose_name="service", max_length=100,  blank=True, null=True)
    slug = models.SlugField()
    image           = models.ImageField(upload_to='images/', verbose_name='image du service', blank=True, null=True)
    image_high      = models.ImageField(upload_to='images/', verbose_name='image_detail_1', blank=True, null=True)
    image_low       = models.ImageField(upload_to='images/', verbose_name="image_detail_2", blank=True, null=True)
    about_high      = tinymce_models.HTMLField(verbose_name='Text service', blank=True, null=True)
    about_low       = tinymce_models.HTMLField(verbose_name='Page service ', blank=True, null=True)
    
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = 'service'
        verbose_name_plural = 'services'

    def get_absolute_url(self):
        return reverse("business:service_detail", kwargs={"slug": self.slug})
