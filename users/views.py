from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserCreationForm
from django.contrib.auth import login


class Register(CreateView):
    template_name = 'registration/registration.html'
    form_class = UserCreationForm
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')