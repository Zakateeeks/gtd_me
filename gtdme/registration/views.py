from django.shortcuts import render
from django.http import HttpResponse


def main_page(request) -> HttpResponse:

    return HttpResponse('<h2>Наталья Петровна и Павел Анатольевич, спокойной ночи!!!</h2>')

def registration(request) -> HttpResponse:

    return HttpResponse('Регистрация')

def authorization(request) -> HttpResponse:

    return HttpResponse('Авторизация')