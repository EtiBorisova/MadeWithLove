from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth import views as auth_views
from django.views import generic as views

from MadeWithLove.accounts.forms import MadeWithLoveUserCreateForm, LoginForm, CreateProfile
from MadeWithLove.accounts.models import MadeWithLoveUser, ProfileModel


class UserRegistration(views.CreateView):
    model = MadeWithLoveUser
    form_class = MadeWithLoveUserCreateForm
    template_name = 'registration_page.html'
    success_url = reverse_lazy('login')

class UserLoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'login-page.html'
    next_page = reverse_lazy('home')


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('login')


class ProfileDetailView(views.DetailView):
    model = ProfileModel
    template_name = 'profile_details_page.html'


class EditProfileView(views.UpdateView):
    model = ProfileModel
    template_name = 'edit_profile_page.html'
    fields = ['email', 'first_name', 'last_name','gender', 'date_of_birth', 'profile_image']

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk':self.object.pk})

class ProfileDeleteView(views.DeleteView):
    model = MadeWithLoveUser


