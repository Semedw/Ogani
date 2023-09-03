from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from user.forms import RegisterForm
from core.models import ProductCategory

# Create your views here.

def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('succes')
    else:
        form = RegisterForm()


    context = {
        'title' : 'Register',
        'form' : form,
        'departments' : ProductCategory.objects.all()
    }
    
    return render(request, 'register.html', context=context)


def succes(request):
    context = {
        'title' : "You've registered succesfully"
    }

    return render(request, 'succes.html', context=context)
