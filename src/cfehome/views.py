import pathlib
from django.http import HttpResponse
from django.shortcuts import render

this_dir = pathlib.Path(__file__).resolve().parent

def home_view(request, *args, **kwargs):
    my_title = "my page"
    my_context = {
        "title": my_title,}
    html_template = "home.html"
    return render(request, html_template,my_context)