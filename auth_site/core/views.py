from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import OpusUser

class RegistroView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "core/registro.html"
    '''
    def form_valid(self, form):
        self.object = form.save()
        print("Mi id es ========== ",self.object.id)
        extendido = OpusUser.objects.get(pk=self.object.id)
        print("extendido ========",extendido)
        return HttpResponseRedirect(self.get_success_url())
    '''
    def get_success_url(self):
        return reverse_lazy('login') + '?register'

def loginView(request):
    return render(request, "core/login.html")

