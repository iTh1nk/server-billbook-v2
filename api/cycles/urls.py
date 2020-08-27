from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('all/', views.CyclesGetPost.as_view()),
    path('single/<int:pk>/', views.CyclesGetPutDelete.as_view())
]
