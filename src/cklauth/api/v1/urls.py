from django.conf.urls import url
from django.conf import settings
from django.views.generic.base import TemplateView
from rest_auth.views import (
    LoginView, LogoutView, UserDetailsView, PasswordChangeView,
    PasswordResetView, PasswordResetConfirmView
)
from rest_auth.registration.views import (
    RegisterView, VerifyEmailView
)
from .views import FacebookLogin

urlpatterns = [
    # URLs that do not require a session or valid token
    url(r'login/$', LoginView.as_view(), name='rest_login'),
    url(r'password/reset/$', PasswordResetView.as_view(), name='rest_password_reset'),
    url(r'password/reset/confirm/$', PasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),

    # URLs that require a user to be logged in with a valid session / token.
    url(r'logout/$', LogoutView.as_view(), name='rest_logout'),
    url(r'user/$', UserDetailsView.as_view(), name='rest_user_details'),
    url(r'password/change/$', PasswordChangeView.as_view(), name='rest_password_change'),

    url(r'registration/$', RegisterView.as_view(), name='rest_register'),
    url(r'registration/verify-email/$', VerifyEmailView.as_view(), name='rest_verify_email'),

    url(r'account-confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(), name='account_confirm_email'),
]

# Social API endpoints
if 'allauth.socialaccount' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'facebook/$', FacebookLogin.as_view(), name='fb_login')
    ]
