from django.views import View
from django.shortcuts import HttpResponse,render,redirect
from .forms import ContactForm
from django.urls import reverse

def home(request):
    template_name = "home.html"
    context={"name":'Home'}
    return render(request,template_name,context)
    

def about(request):
    template_name = "About.html"
    context={"name":'About'}
    return render(request,template_name,context)


def contact(request):
    template_name = "contact.html"
    contact_form = ContactForm()
    context={"name":'Contact','contactform':contact_form}
    return render(request,template_name,context)

def products(request):
    template_name = "products.html"
    context={"name":'Products'}
    return render(request,template_name,context)

def validateform(request):
    if request.method ==  'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()            
    return redirect(reverse('home'))
    