#Django
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginView(LoginView):
    """Login del sistema"""
    template_name = 'login.html'

    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


    
class CrearCitas(TemplateView):
    template_name = 'SenaSoftPython/Citas.html'

