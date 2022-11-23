from django.urls import path
from . import views

app_name = "TodoAPP"
urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    # path("read/", views.read, name="read"),
    path("delete/<int:pk>", views.delete, name="delete"),
]
