"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from menu.views import MainMenuView
from vacancy.views import VacancyListView
from resume.views import ResumeListView, ResumeSignupView, ResumeLoginView
from django.views.generic import RedirectView

urlpatterns = [
    path('', MainMenuView.as_view()),
    path('vacancies/', VacancyListView.as_view()),
    path('resumes/', ResumeListView.as_view()),
    path('admin/', admin.site.urls),
    #path('signup/', ResumeSignupView.as_view()),
    #path('login/', ResumeLoginView.as_view()),
    path('login/', RedirectView.as_view(url='/login')),
    path('signup/', RedirectView.as_view(url='/signup')),
]
