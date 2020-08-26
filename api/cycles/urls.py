from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('get-post/', views.CyclesGetPost.as_view())
]
