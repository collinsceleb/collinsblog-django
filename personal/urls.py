from django.urls import path

from personal.views import home_view
from . import views

app_name = 'personal'
urlpatterns = [
    path('', home_view, name="home"),

]
