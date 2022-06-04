from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView

from .forms import *
from .models import *
from .utils import *


class VacancyHome(DataMixin, ListView):
    model = Vacancy
    template_name = 'searcherapp/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Vacancy.objects.filter(is_published=True)

class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'searcherapp/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Контакты")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')




class About(DataMixin, ListView):
    model = Startup
    template_name = 'searcherapp/about.html'
    context_object_name = 'about'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Что такое - FindWorkUa ")
        return dict(list(context.items()) + list(c_def.items()))

class StartupHome(DataMixin, ListView):
    model = Startup
    template_name = 'searcherapp/startup.html'
    context_object_name = 'startup'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Страница по Startup")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Startup.objects.filter(is_published=True)


class AddStartup(DataMixin, LoginRequiredMixin, CreateView):
    form_class = AddStartupPostForm
    template_name = 'searcherapp/addpage_startup.html'
    success_url = reverse_lazy('home')
    login_url = '/admin/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление startup")
        return dict(list(context.items()) + list(c_def.items()))

class ShowStartup(DataMixin, DetailView):
    model = Startup
    template_name = 'searcherapp/startup_post.html'
    slug_url_kwarg = 'startup_slug'
    context_object_name = 'startup_post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['startup_post'])
        return dict(list(context.items()) + list(c_def.items()))


class AddPage(DataMixin, LoginRequiredMixin, CreateView):
    form_class = AddPostForm
    template_name = 'searcherapp/addpage.html'
    success_url = reverse_lazy('home')
    login_url = '/admin/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление вакансии")
        return dict(list(context.items()) + list(c_def.items()))



class ShowPost(DataMixin, DetailView):
    model = Vacancy
    template_name = 'searcherapp/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class VacancyCategory(DataMixin, ListView):
    model = Vacancy
    template_name = 'searcherapp/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Vacancy.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'searcherapp/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'searcherapp/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')