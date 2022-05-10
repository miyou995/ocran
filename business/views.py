from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import ContactForm, QuoteForm, HiringForm
from .models import Bien, Contact, Formule, Quote, Hiring, Surface
from django.utils.translation import gettext as _
# Create your views here.
from django.contrib import messages

###index 
class IndexView(TemplateView):
    template_name= "index.html"
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["formules"] =Formule.objects.all()
        context["biens"] = Bien.objects.all()
        context["surfaces"] =Surface.objects.all()
        return context
##présentation
class AboutView(TemplateView):
    template_name= "presentation.html"
##services
class ServiceView(TemplateView):
    template_name= "services.html"

class MaisonView(TemplateView):
    template_name= "services-1.html"
    
class OfficeView(TemplateView):
    template_name= "services-2.html"

class CopView(TemplateView):
    template_name= "services-3.html"

class DesView(TemplateView):
    template_name= "services-4.html"
    
class RemView(TemplateView):
    template_name= "services-5.html"
## CONTACT 

class ContactView(SuccessMessageMixin, CreateView):
    template_name= "contact.html"
    form_class= ContactForm
    model = Contact 
    success_message = "Votre message a été envoyé avec succès, un e-mail vous sera envoyé prochainement."
    success_url = reverse_lazy('business:contact')
   
    def form_valid(self, form):
        form.send_email() 
        return super().form_valid(form)
    
      

## devis

class QuoteoView(SuccessMessageMixin, CreateView):
    template_name= "quote.html"
    form_class= QuoteForm
    model = Quote 
    success_message = "Un e-mail contenant les informations demandé vous a été envoyé."
    success_url = reverse_lazy('business:quote')
    def form_valid(self, form):
        form.send_email()   
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super(QuoteoView, self).get_context_data(**kwargs)
        context["formules"] =Formule.objects.all()
        context["biens"] = Bien.objects.all()
        context["surfaces"] =Surface.objects.all()
        return context
   
#recrutements
class RecruitingView(SuccessMessageMixin, CreateView):
    template_name= "recrutement.html"
    form_class= HiringForm
    model = Hiring 
    success_message = "Votre demande a été soumise, Un e-mail vous sera envoyé prochainement." 
    success_url = reverse_lazy('business:recruiting')
    def form_valid(self, form):
        form.send_email() 
        return super().form_valid(form)

##email
class EmailView(TemplateView):
    template_name= "email.html"
    
    
def create_quote(request):
    context = {}
    context["formules"] =Formule.objects.all()
    context["biens"] = Bien.objects.all()
    context["surfaces"] =Surface.objects.all()
    form = QuoteForm()
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.send_email() 
            quote = form.save()
            print('sdvvdvsdv',quote)
            # print(form)
        total_cost = quote.get_total_cost()
        print('total', total_cost)
        messages.success(request, f'le service que vous avez demandé à un cout approximatif de  <strong>{total_cost}</strong> DA. ')
        if request.htmx:
            return render(request, 'snippets/message.html', context)
        # return HttpResponse(f'{quote.get_total_cost()}')
    return render(request, 'quote.html', context)
#     <div class="alert alert-primary" role="alert">
#   This is a primary alert—check it out!
# </div>
