from django.shortcuts import render, redirect

from django.contrib.auth import (
    authenticate,
    login,
    logout,


)
from . forms import UserLogInForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Document
# Create your views here.


class DocumentCreateView(CreateView):
    model = Document
    fields = ['upload', ]
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        documents = Document.objects.all()
        context['documents'] = documents
        return context


@login_required(login_url='/kac/login')
def index(request):
    return render(request, 'index.html')


def login_view(request):
    form = UserLogInForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('kac:index')
        # print(request.user.is_authenticated())
    return render(request, 'kac/loginPage.html', {'form': form})


def register_view(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect("kac:index")

    return render(request, 'kac/registerPage.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect("kac:index")
