from django.shortcuts import render
from django.views import View
from resume.models import Resume
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from utility.loger import log_action


class ResumeListView(View):
    def get(self, request, *args, **kwargs):
        log_action(request)
        return render(request, 'resume/resume_list.html', {'resume': Resume.objects.all()})


class ResumeSignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'resume/signup.html'


class ResumeLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    success_url = '/'
    template_name = 'resume/login.html'



