from django.urls import path
from .views import PasswordListView, PasswordDeleteView
from . import views

urlpatterns = [
    path('generate/', views.save_password, name="generatepassword"),
    path('password_list/', PasswordListView.as_view(), name="password_list"),
    path('delete/<int:pk>/', PasswordDeleteView.as_view(), name="delete_password")
]
