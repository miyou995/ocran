from django.contrib import admin
from .models import Contact, Quote, Hiring, Formule, Surface,  Bien

# Register your models here.

admin.site.register(Surface) 
admin.site.register(Contact) 
admin.site.register(Quote) 
admin.site.register(Hiring) 
admin.site.register(Formule) 
admin.site.register(Bien) 

