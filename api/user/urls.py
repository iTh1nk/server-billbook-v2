from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.UserRegistrationView.as_view()),
    path('login/', views.UserLoginView.as_view()),
    path('profile/', views.UserProfileView.as_view()),
    path('get/', views.UserList.as_view())
]
