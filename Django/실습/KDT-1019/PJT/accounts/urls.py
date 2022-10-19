from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('<int:pk>/', views.detail, name="detail"),
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]
