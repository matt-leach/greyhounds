from django.http import HttpResponse
from django.shortcuts import render




def home(request):
    context = {}
    return render(request, 'base.html', context)



def just_render(request, template):
    """
        View that takes a template name and just renders it
    """
    return render(request, template, {})