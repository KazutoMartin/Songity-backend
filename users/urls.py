from django.urls import path

from users.views import UserInitApi, get_user


urlpatterns = [
    path('init/', UserInitApi.as_view(), name='init'),
    path('get-user/', get_user, name='get_user'),
]