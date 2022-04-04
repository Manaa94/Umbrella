from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from weather.models import City
from django.views.generic import View
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView, ListView
from weather.forms import SignUpForm, CityForm, UserForm
from django.contrib.auth import logout
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

    def get(self, request):
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


class LogoutUserView(View):
    def get(self, request):
        logout(request)
        return redirect('weather:login')


class UpdateUserView(UpdateView):
    template_name = 'edit.html'
    form_class = UserForm
    queryset = User.objects.all()

    def get_success_url(self):
        return reverse('weather:profile')


# User search history
class HistoryView(ListView):
    template_name = 'profile.html'
    model = User
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['history'] = 'history'
        context['form'] = CityForm()
        return context

    def get_queryset(self):
        user = User.objects.get(pk=self.kwargs['pk'])
        return user.cities.order_by('-searched_at')
