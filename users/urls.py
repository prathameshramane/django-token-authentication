from django.urls import path

from .views import RegisterView, LoginView, UserInformationView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserInformationView.as_view()),
]
