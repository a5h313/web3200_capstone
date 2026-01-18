from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def landing(request: HttpRequest) -> HttpResponse:
    html = """
    <h1>WST</h1>
    <p>Welcome to WST: Weber State Univ. Trade</p>
    """
    return HttpResponse(html)