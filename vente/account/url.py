from django.urls import path
from account.views import signup,connexion
from django.contrib.auth import views
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView

urlpatterns = [
 path('',signup,name='signup'),
 path('connexion',connexion,name='connexion'),
 path('reset_password',views.PasswordResetView.as_view(template_name='account/password_reset.html'),name='reset_password'),
 path('password_reset_send',views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),name='password_reset_done'),
 path('reset/<uidb64>/<token>',views.PasswordResetConfirmView.as_view(template_name='account/password_confirm.html'),name='password_reset_confirm'),
 path('reset_password_complete',views.PasswordResetCompleteView.as_view(template_name='account/password_complete.html'),name='password_complete'),
 path('change',PasswordChangeView.as_view(template_name='account/change_password.html',
                                             
          success_url='confirme'),name='change_password'),
    path('confirme',PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'),name='confirme'),
]
