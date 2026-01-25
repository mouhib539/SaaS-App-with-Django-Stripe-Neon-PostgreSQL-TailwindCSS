import pathlib
from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_view(request, *args, **kwargs):
    queryset = PageVisit.objects.filter(path=request.path)
    my_title = "my page"
    my_context = {
        "title": my_title,
        "queryset": queryset}
    html_template = "home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template,my_context) 

def about_view(request, *args, **kwargs):
    queryset = PageVisit.objects.all()
    my_title = "about page"
    my_context = {
        "title": my_title,
        "queryset": queryset
    }
    html_template = "about.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template,my_context)