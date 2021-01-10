from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.urls import reverse
from django.views import generic
from django.views.generic import UpdateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, User

from home.forms import SignUpForm
from home.models import Profile
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
            user.profile.location = form.cleaned_data.get('location')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def view_profile(request, name=None):
    if name:
        user = User.objects.get(username=name)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'profile.html', args)

class EditProfileForm(generic.UpdateView):
    model = Profile
    template_name='edit_profile.html'
    fields = [
            'bio', 'location', 'birth_date', 'facebook_url', 'twitter_url', 'instagram_url', 'image',
    ]

    def get_object(self):
        return self.request.user

'''def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)'''
\


