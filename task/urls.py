from django.urls import path

from . import views

app_name = "task"
urlpatterns = [
    path(route="", view=views.home, name="home"),
    path(route="create/", view=views.create, name="create"),
    path(route="update/<int:pk>/", view=views.update, name="update"),
    path(route="delete/<int:pk>/", view=views.delete, name="delete"),
]
