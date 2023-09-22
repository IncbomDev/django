from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm  
from django.contrib.auth.decorators import login_required


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm  # Use the custom form
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def my_page_view(request):
    if request.user.is_authenticated:
        return render(request, 'my_page_logged_in.html')
    else:
        return render(request, 'my_page_not_logged_in.html')
    