from django.urls import path

from users import views

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path("user/",views.UserDetailAPI.as_view()),
    path('register/',views.RegisterUserAPIView.as_view()),
]

