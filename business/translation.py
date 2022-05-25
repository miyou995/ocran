
from modeltranslation.translator import translator, TranslationOptions
from .models import Bien, Formule, About, Service, Business



class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'about_high', 'about_low')

translator.register(Service, ServiceTranslationOptions)


class AboutTranslationOptions(TranslationOptions):
    fields = ('name', 'about_high', 'about_low', 'title')

translator.register(About, AboutTranslationOptions)


class BusinessTranslationOptions(TranslationOptions):
    fields = ('name','title', 'adress', 'about', 'about_2', 'mini_about')

translator.register(Business, BusinessTranslationOptions)

class FormuleTranslationOptions(TranslationOptions):
    fields = ('formule','description')

translator.register(Formule, FormuleTranslationOptions)


class BienTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Bien, BienTranslationOptions)