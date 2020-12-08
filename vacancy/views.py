from django.shortcuts import render
from django.views import View
from vacancy.models import Vacancy
from utility.loger import log_action


class VacancyListView(View):
    def get(self, request, *args, **kwargs):
        log_action(request)
        return render(request, 'vacancy/vacancy_list.html', {'vacancy': Vacancy.objects.all()})

