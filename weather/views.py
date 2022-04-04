from django.urls import reverse
from django.views.generic import CreateView
from weather.forms import SignUpForm
from .utils import get_data
from dotenv import load_dotenv

load_dotenv()


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'index.html'

    def get_success_url(self):
        return reverse('weather:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for key, value in get_data('tehran').items():
            context[key] = value
        return context
