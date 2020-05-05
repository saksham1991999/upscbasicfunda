from django.shortcuts import render
from . import models, serializers
from rest_framework import viewsets


class CurrentAffairViewSet(viewsets.ModelViewSet):
    queryset = models.CurrentAffair.objects.all()
    serializer_class = serializers.CurrentAffairSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = models.Video.objects.all()
    serializer_class = serializers.VideoSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer

class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = models.Newsletter.objects.all()
    serializer_class = serializers.NewsletterSerializer

class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = models.ContactUs.objects.all()
    serializer_class = serializers.ContactUsSerializer

class EventRegistrationViewSet(viewsets.ModelViewSet):
    queryset = models.EventRegistration.objects.all()
    serializer_class = serializers.EventRegistartionSerializer


