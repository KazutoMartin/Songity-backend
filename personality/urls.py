from django.urls import path

from .views import new_personality

urlpatterns = [
    path('new-personality/', new_personality),
]