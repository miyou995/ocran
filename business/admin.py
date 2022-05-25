from django.contrib import admin
from .models import Contact, Quote, Hiring, Formule, Surface,  Bien, Business, About, Slide, Service

# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {"slug": ("name",)}
    exclude= ('name_fr','about_high_fr', 'about_low_fr')
    list_display_links = ('id','name')
    list_per_page = 40
admin.site.register(Service, ServiceAdmin)


class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    exclude= ('name_fr','about_high_fr', 'about_low_fr', 'title_fr')
    list_display_links = ('id','name')
    list_per_page = 40
admin.site.register(About, AboutAdmin)

class BusinessAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    exclude= ('name_fr','title_fr', 'adress_fr', 'about_fr', 'about_2_fr', 'mini_about_fr')
    list_display_links = ('id','name')
    list_per_page = 40
admin.site.register(Business, BusinessAdmin)

class FormuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'formule', 'price')
    exclude= ('formule_fr','description_fr')
    list_display_links = ('id','formule')
    list_editable = [ 'price']
    list_per_page = 40
admin.site.register(Formule, FormuleAdmin)

class BienAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    exclude= ('name_fr',)
    list_display_links = ('id','name')
    list_editable = [ 'price']
    list_per_page = 40
admin.site.register(Bien, BienAdmin)

class SurfaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'surface', 'price')
    exclude= ('surface_fr',)
    list_display_links = ('id','surface')
    list_editable = [ 'price']
    list_per_page = 40
admin.site.register(Surface, SurfaceAdmin)

admin.site.register(Contact) 
admin.site.register(Quote) 
admin.site.register(Hiring) 
admin.site.register(Slide) 