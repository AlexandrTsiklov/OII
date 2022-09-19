from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from KILL_EXPERT_SYSTEM.EXPERTA_BRAIN import check_skills


def show_form(request):
    return render(request, 'experta.html')


def calculate_skills(request):
    return JsonResponse(check_skills(dict(request.GET)))