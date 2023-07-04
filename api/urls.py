from django.urls import path
from . import views


urlpatterns = [
    path('todos/', views.TodoListCreate.as_view()),
    path('todos/<int:pk>/', views.TodoUpdate.as_view()),
    path('todos/<int:pk>/status/', views.TodoStatus.as_view()),
    path('signup/', views.signup),
    path('login/', views.login),
]
