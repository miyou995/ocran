from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, ListView , DetailView
from django.views.generic.edit import CreateView
from .forms import ContactForm, QuoteForm, HiringForm
from .models import Bien, Contact, Formule, Quote, Hiring, Surface, Slide, About, Service
from django.utils.translation import gettext as _
# Create your views here.
from django.contrib import messages
from django.shortcuts import redirect
###index 
class IndexView(TemplateView):
    template_name= "index.html"
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["formules"] =Formule.objects.all()
        context["services"] =Service.objects.all()
        context["slide"] =Slide.objects.last()
        context["biens"] = Bien.objects.all()
        context["surfaces"] =Surface.objects.all()
        return context


##ABOUT
class AboutView(TemplateView):
    template_name= "about.html"
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context["abouts"] =About.objects.all()
        return context

##services

class ServiceView(ListView):
    template_name= "services.html"
    model = Service
    context_object_name ="services"

class ServiceDetail(DetailView):
    model = Service
    template_name='services_detail.html' 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] =Service.objects.all()
        return context


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

    def form_invalid(self, form):
        messages.error(self.request,form.errors)
        return redirect('business:recruiting')

    

    
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
        messages.success(request, f'Un agent vous contactera prochainement avec un appel téléphonique ou un e-mail contenant les informations demandées.')
        if request.htmx:
            return render(request, 'snippets/message.html', context)
        # return HttpResponse(f'{quote.get_total_cost()}')
    return render(request, 'quote.html', context)


# le service que vous avez demandé à un cout approximatif de  <strong>{total_cost}</strong> DA.    
# <div class="alert alert-primary" role="alert">
#   This is a primary alert—check it out!
# </div>


