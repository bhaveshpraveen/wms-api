from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver


# pass : a9789959296b


class Reading(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    owner = models.ForeignKey('auth.User', related_name='api', on_delete=models.CASCADE, null=False)
    temperature = models.FloatField(default=0, null= False)
    pressure = models.FloatField(default=0, null=False)
    humidity = models.FloatField(default=0, null=False)
    updated = models.DateTimeField(auto_now=True, null=False)

    # def __str__(self):
    #     return 'Temperature = {}\nPressure = {}\nHumidity = {}'.format(str(self.temperature), str(self.pressure), str(self.humidity))



@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)