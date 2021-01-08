from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from home.forms import SignUpForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def info(request):
    return render(request, 'info.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
def profile(request):
    return render(request, 'profile.html')

class UserEditProfileView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

