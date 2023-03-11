from django.shortcuts import render


def index(request):
    return render(request, 'authorize/index.html')


def sign_up(request):
    return render(request, 'authorize/sign_up.html')


def sign_in(request):
    return render(request, 'authorize/sign_in.html')

