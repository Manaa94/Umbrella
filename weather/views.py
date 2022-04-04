from django.urls import reverse
from django.shortcuts import render
from weather.models import City
from django.views.generic import View
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from weather.forms import SignUpForm, CityForm
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


class LoginUserView(LoginView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['res'] = 'res'
        for key, value in get_data('tehran').items():
            context[key] = value
        return context

class ProfileView(View):

    def get(self,request):
        context = {'form': CityForm()}
        for key, value in get_data('tehran').items():
            context[key] = value
        return render(request, 'profile.html', context)

    def post(self, request):
        form = CityForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            city = City(name=form.cleaned_data['name'])
            city.save()
            city.user.add(request.user)
            city.save()
            context['form'] = CityForm()
            try:
                for key, value in get_data(form.cleaned_data['name']).items():
                    context[key] = value
            except:
                context['error'] = 'error'
        return render(request, 'profile.html', context)
