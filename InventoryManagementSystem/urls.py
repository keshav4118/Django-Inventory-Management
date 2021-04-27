from django.contrib import admin
from django.urls import path,include
from user import views as user_views
from django.contrib.auth import views as auth_view

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('register/',user_views.register, name='user-register'),
    path('',auth_view.LoginView.as_view(template_name='user/login.html'),name= 'user-login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='user/logout.html'),name= 'user-logout'),
    path('profile/',user_views.profile, name='user-profile'),
    path('profile_update/',user_views.profile_update, name='user-profile-update'),
    path('password_reset/',auth_view.PasswordResetView.as_view(template_name='user/password_reset.html'),name='password_reset'),
    path('password_reset_done/',auth_view.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>',auth_view.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete/',auth_view.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),name='password_reset_complete')



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)