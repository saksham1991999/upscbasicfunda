from django.db import models

# Create your models here.
class CurrentAffair(models.Model):
    name = models.CharField(max_length = 128)
    image = models.ImageField()
    pdf = models.FileField()
    date = models.DateField(auto_now_add=True)


class Video(models.Model):
    name = models.CharField(max_length=128)
    url = models.CharField(max_length=256)
    

class Event(models.Model):
    name = models.CharField(max_length=128)
    details = models.TextField()
    image = models.ImageField()
    event_date = models.DateField()
    date = models.DateField(auto_now_add=True)

class Newsletter(models.Model):
    email = models.EmailField()

class ContactUs(models.Model):
    name = models.CharField(max_length=80)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'Contact Us'

class EventRegistration(models.Model):
    event = models.ForeignKey('core.Event', on_delete=models.PROTECT)
    name = models.CharField(max_length=128)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
