from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


class RegisterView(CreateView):
    '''Render registration information'''
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = '../templates/registration/register.html'