from django.urls import path

from users import views

urlpatterns = [
    path('login/', views.LoginView.as_view()),
]