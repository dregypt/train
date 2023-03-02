from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(_('phone'), max_length=15, blank=True, null=True)
    state = models.CharField(_('state'), max_length=50, blank=True, null=True)
    city = models.CharField(_('city'), max_length=50, blank=True, null=True)
    address = models.CharField(_('address'), max_length=200, blank=True, null=True)


    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


