from django.shortcuts import render,redirect
from django.template.loader import get_template

from django.http import HttpResponse
# Create your views here.
def tool_page(request):
    context = {}
    return render(request, 'tool_page.html', context)
    # return HttpResponse("<h1>njkhjk</h1>")