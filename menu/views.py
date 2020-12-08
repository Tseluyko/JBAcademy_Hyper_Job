from django.shortcuts import render
from django.views import View
from vacancy.models import Vacancy
from resume.models import Resume
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from django.views.generic.base import TemplateView
from utility.loger import log_action


class MainMenuView(View):
    def get(self, request, *args, **kwargs):
        log_action(request)
        context = dict()
        if not request.user.is_authenticated:
            context['user_type'] = 'none'
        elif request.user.is_staff:
            context['user_type'] = 'staff'
        else:
            context['user_type'] = 'user'
        return render(request, 'menu/main_menu.html', context=context)


class VacancyNewView(View):
    def get(self, request, *args, **kwargs):
        log_action(request)
        return render(request, 'menu/new_item.html')

    def post(self, request, *args, **kwargs):
        log_action(request)
        if not request.user.is_authenticated:
            raise PermissionDenied
        if not request.user.is_staff:
            raise PermissionDenied
        Vacancy.objects.create(description=request.POST.get("description"),
                               author=request.user)
        return redirect('/')


class ResumeNewView(View):
    def get(self, request, *args, **kwargs):
        log_action(request)
        return render(request, 'menu/new_item.html')

    def post(self, request, *args, **kwargs):
        log_action(request)
        if not request.user.is_authenticated:
            raise PermissionDenied
        if request.user.is_staff:
            raise PermissionDenied
        Resume.objects.create(description=request.POST.get("description"),
                               author=request.user)
        return redirect('/')

