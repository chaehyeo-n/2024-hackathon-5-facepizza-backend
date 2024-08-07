from django.urls import path, include
from .views import RegisterView, LoginView, LogoutView, DeleteUserView

app_name = 'accounts'

urlpatterns = [
    path('accounts/register', RegisterView.as_view()),
    path('accounts/login', LoginView.as_view()),
    path('accounts/logout', LogoutView.as_view()),
    path('delete/', DeleteUserView.as_view(), name='delete-user'),
]