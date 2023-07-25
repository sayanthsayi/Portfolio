from django.shortcuts import render,redirect
from . models import contact
from . forms import ContactForm
from django . contrib import messages

# Create your views here.


def home(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Thankyou For The Message ")
            return redirect('home')
    context = {'form':form}
    return render(request,"home.html",context)
