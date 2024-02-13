
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView,FormView

from app.forms import *

class TemplateHtml(TemplateView):
    template_name='TemplateHtml.html'
    
    def get_context_data(self, **kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['name']='Monisha'
        ECDO['age']=21
        return ECDO

class insertschoolbyfv(FormView):
    template_name='insertschoolbyfv.html'
    form_class=SchoolForm

    def form_valid(self, form): 
        form.save()
        return HttpResponse('insertschoolbyfv is done')

