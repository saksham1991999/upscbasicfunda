from rest_framework import serializers
from . import models

class CurrentAffairSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="inquiry-detail")

    class Meta:
        model = models.CurrentAffair
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="inquiry-detail")

    class Meta:
        model = models.Video
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="inquiry-detail")

    class Meta:
        model = models.Event
        fields = '__all__'


class NewsletterSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="inquiry-detail")

    class Meta:
        model = models.Newsletter
        fields = '__all__'

class ContactUsSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="inquiry-detail")

    class Meta:
        model = models.ContactUs
        fields = '__all__'

class EventRegistartionSerializer(serializers.Serializer):
    # url = serializers.HyperlinkedIdentityField(view_name="inquiry-detail")
    event = EventSerializer()

    class Meta:
        model = models.EventRegistration
        fields = '__all__'



