from django.shortcuts import render
from django.views import View


class MainMenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'menu/main_menu.html')
