from django.shortcuts import render
from django.views import View
from vacancy.models import Vacancy

class VacancyListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancy/vacancy_list.html', {'vacancy': Vacancy.objects.all()})
