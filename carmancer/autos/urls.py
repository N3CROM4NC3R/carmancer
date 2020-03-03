from django.urls import path
from autos import views
urlpatterns = [
    path(
        route='',
        view=views.hello_world,
        name="hello_world")
]