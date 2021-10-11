from django.urls import path
from . import views

urlpatterns = [
    path("first", views.fun1),
    path("second", views.fun2,name="srinitha"),
]
