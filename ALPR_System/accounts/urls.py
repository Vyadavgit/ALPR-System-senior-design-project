from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.homeFn, name="home"),
    path('login/', views.loginFn, name="login"),
    path('register/', views.registerFn, name = "register"),
    path('logout/', views.logoutFn, name = "logout"),

    path('update_vehicle/<str:pk>', views.updateVehicle, name="update_vehicle"),
    path('delete_vehicle/<str:pk>', views.deleteVehicle, name="delete_vehicle"),
    path('delete_resident/<str:pk>', views.deleteResident, name="delete_resident"),

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

    path('edit_profile/', views.editProfileFn, name="edit_profile"),
    path('register_vehicle/', views.registerVehicleFn, name="register_vehicle"),
    

]