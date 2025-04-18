from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path(route='profile/', view=views.profile, name='profile'),
    path(route='signup/', view=views.SignUpView.as_view(), name='signup'),
    path(
        route='<int:pk>/<str:username>/update/',
        view=views.update,
        name='update',
    ),
]
