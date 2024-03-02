from django.urls import path

from .views import login_view

appname = 'myauth'

urlpatterns = [
    path("login/", login_view, name='login'),
]