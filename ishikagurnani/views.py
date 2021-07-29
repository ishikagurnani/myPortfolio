from django.http import HttpResponse
from django.shortcuts import redirect, render
from . import forms

# Create your views here.
def index(request):
    return render(request, "ishikagurnani/home.html")

def contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = forms.ContactForm
    context = {'form': form}
    return render(request, "ishikagurnani/contact.html", context)