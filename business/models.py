from django.db import models
from django.urls import reverse
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
    email       = models.EmailField(verbose_name="E-mail")
    phone       = models.CharField(verbose_name="Téléphone" , max_length=25)
    birth_date  = models.DateField() 
    birth_place = models.CharField(max_length=150, verbose_name='lieu de naissance')
    message     = models.TextField(verbose_name='experience')
    cv_file     = models.FileField(upload_to='media', verbose_name='CV', null=True, blank=True)

    class Meta:
        verbose_name = _("hiring")
        verbose_name_plural = _("hirings")

    def __str__(self):
        return self.email

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