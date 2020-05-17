from django.shortcuts import render
from . import models, serializers
from rest_framework import viewsets, permissions


class CurrentAffairViewSet(viewsets.ModelViewSet):
    queryset = models.CurrentAffair.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.CurrentAffairSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = models.Video.objects.all()
    serializer_class = serializers.VideoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EventViewSet(viewsets.ModelViewSet):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = models.Newsletter.objects.all()
    serializer_class = serializers.NewsletterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = models.ContactUs.objects.all()
    serializer_class = serializers.ContactUsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EventRegistrationViewSet(viewsets.ModelViewSet):
    queryset = models.EventRegistration.objects.all()
    serializer_class = serializers.EventRegistartionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


