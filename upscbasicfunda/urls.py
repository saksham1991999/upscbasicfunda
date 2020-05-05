
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
import rest_framework
from core.views import CurrentAffairViewSet, VideoViewSet, EventViewSet, NewsletterViewSet, ContactUsViewSet, EventRegistrationViewSet

router = routers.DefaultRouter()
router.register('current-affairs',CurrentAffairViewSet, basename='current-affairs')
router.register('videos',VideoViewSet, basename='videos')
router.register('events',EventViewSet, basename='events')
router.register('newsletter',NewsletterViewSet, basename='newsletter')
router.register('contact-us',ContactUsViewSet, basename='contact-us')
router.register('event-registrations',EventRegistrationViewSet, basename='event-registrations')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)