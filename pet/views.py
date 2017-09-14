from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, RedirectView, CreateView, FormView

from pet.forms import RegistrationForm, LoginForm


class HomePageView(TemplateView):
    template_name = 'index.html'


class RegisterView(CreateView):
    model=User
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('home', args=[])

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data.get('password'))
        user.save()
        return super().form_valid(form)

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('home', args=[])

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user and user.is_active :
            login(self.request, user)
            return redirect(self.success_url)
        else:
            return self.form_invalid(form)

    
class LogoutView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'home'

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)

