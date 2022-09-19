from django.contrib import admin
from django.urls import path

from KILL_EXPERT_SYSTEM.views import show_form, calculate_skills


urlpatterns = [
    path('admin/', admin.site.urls),
    path('experta', show_form),
    path('calculate-skills', calculate_skills)
]
