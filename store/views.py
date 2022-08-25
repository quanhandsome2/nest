from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, "contact_us.html")

def team(request):
    return render(request, "team.html")