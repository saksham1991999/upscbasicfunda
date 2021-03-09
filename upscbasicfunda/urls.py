
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
import rest_framework
from core.views import FacebookLogin
from core.views import GoogleLogin
router = routers.DefaultRouter()

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('rest-auth/google/', GoogleLogin.as_view(), name='google_login'),

    path('admin/', admin.site.urls),
    #path('accounts/password/reset/',auth_views.password_reset,{'post_reset_redirect': reverse_lazy('auth_password_reset_done'),'html_email_template_name': 'registration/password_reset_html_email.html'},name='auth_password_reset'),
    path('accounts/', include('allauth.urls')),
    path('nested_admin', include('nested_admin.urls')),
    path('api/core/', include('core.urls', namespace='core')),
    path('api/blog/', include('blog.urls', namespace='blog')),
    path('api/quiz/', include('quiz.urls', namespace='quiz')),
    path('api/cart/', include('cart.urls', namespace='cart')),
    
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
    #path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_form.html'), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    #path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),
]

urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)