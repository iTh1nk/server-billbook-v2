from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('get/', views.GetAll.as_view()),
    path('post/', views.PostAll.as_view()),
    path('get/<int:pk>/', views.GetAny.as_view()),
    path('put/<str:token>/', views.PutLastUsed.as_view()),
    path('delete/<int:pk>/', views.DeleteAny.as_view())
]
