from django.shortcuts import render, redirect
from .models import Finch
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import FeedingForm
# Add the following import
# from django.http import HttpResponse


# class Finch:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, breed, description, age):
#     self.name = name
#     self.breed = breed
#     self.description = description
#     self.age = age

# finches = [
#   Finch('Lolo', 'tabby', 'foul little demon', 3),
#   Finch('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
#   Finch('Raven', 'black tripod', '3 legged cat', 4)
# ]



# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html') 

def finches_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', { 'finches': finches })

class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'

class FinchUpdate(UpdateView):
  model = Finch
  fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches/'

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  feeding_form = FeedingForm()
  return render(request, 'finches/detail.html', {
     'finch': finch, 'feeding_form': feeding_form 
  })

def add_feeding(request, finch_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)  
