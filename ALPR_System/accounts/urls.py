from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.homeFn, name="home"),
    path('login/', views.loginFn, name="login"),
    path('register/', views.registerFn, name = "register"),
    path('logout/', views.logoutFn, name = "logout"),
    path('add_resident/', views.addResident, name = "add_resident"),
    #path('add_vehicle/', views.addVehicle, name = "add_vehicle"),
    # path('update_vehicle/', views.updateVehicle, name="update_vehicle"),
    # path('delete_vehicle/', views.deleteVehicle, name="delete_vehicle"),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="accounts/reset_Password.html"),
         name="reset_password"),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="accounts/sent_reset_Email.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_Confirmation.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="accounts/reset_Complete.html"),
         name="password_reset_complete"),

    path('dashboard/', views.dashboardFn, name="dashboard"),

]