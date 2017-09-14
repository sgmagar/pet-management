from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, RedirectView, CreateView, FormView, UpdateView, DeleteView

from pet.forms import RegistrationForm, LoginForm, DogForm, CatForm
from pet.models import Dog, Cat


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['dogs'] = self.get_dogs()
        ctx['cats'] = self.get_cats()
        return ctx

    def get_dogs(self):
        if self.request.user.is_authenticated():
            return Dog.objects.filter(owner=self.request.user)
        return []

    def get_cats(self):
        if self.request.user.is_authenticated():
            return Cat.objects.filter(owner=self.request.user)
        return []


class CreateDogView(LoginRequiredMixin, CreateView):
    model = Dog
    form_class = DogForm
    template_name = 'create_dog.html'
    success_url = reverse_lazy('home', args=[])

    def form_valid(self, form):
        dog = form.save(commit=False)
        dog.owner = self.request.user
        dog.save()
        return super().form_valid(form)


class EditDogView(LoginRequiredMixin, UpdateView):
    model = Dog
    form_class = DogForm
    template_name = 'create_dog.html'
    success_url = reverse_lazy('home', args=[])

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)


class DeleteDogView(LoginRequiredMixin, DeleteView):
    model = Dog
    success_url = reverse_lazy('home', args=[])

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)

    def get(self, request, *args, **kwargs):
        dog = get_object_or_404(self.get_queryset(), id=kwargs.get('pk'))
        dog.delete()
        return redirect(self.success_url)


class CreateCatView(LoginRequiredMixin, CreateView):
    model = Cat
    form_class = CatForm
    template_name = 'create_cat.html'
    success_url = reverse_lazy('home', args=[])

    def form_valid(self, form):
        cat = form.save(commit=False)
        cat.owner = self.request.user
        cat.save()
        return super().form_valid(form)


class EditCatView(LoginRequiredMixin, UpdateView):
    model = Cat
    form_class = CatForm
    template_name = 'create_cat.html'
    success_url = reverse_lazy('home', args=[])

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)


class DeleteCatView(LoginRequiredMixin, DeleteView):
    model = Cat
    success_url = reverse_lazy('home', args=[])

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)

    def get(self, request, *args, **kwargs):
        cat = get_object_or_404(self.get_queryset(), id=kwargs.get('pk'))
        cat.delete()
        return redirect(self.success_url)

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

