from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User


class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.email


def upload_to(instance, filename):
    return '/'.join(['images', unicode(instance.pk), filename])
