from django.urls import path
from . import views

urlpatterns = [
    path('detect/', views.detectFn, name="detect"),
    path('notifications/', views.notificationsFn, name="notifications"),
]

