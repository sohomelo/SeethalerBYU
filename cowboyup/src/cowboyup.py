'''
Created on Aug 30, 2017

@author: j_see
'''
from django.http import HttpRequest
from django.shortcuts import render
from src.myforms import MyForm

def cowboyup(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MyForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpRequest('/thanks/')
    
    # if a GET (or any other method) we'll create a blank form
    else:
        form = MyForm()
    
        return render(request, 'form.html', {'form': form})


