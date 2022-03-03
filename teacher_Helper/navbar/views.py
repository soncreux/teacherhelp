from django.shortcuts import render


def navbar(request):
    return render(request, 'navbar/navbar.html', {})
# Create your views here.
