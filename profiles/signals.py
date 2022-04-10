from django.contrib.auth.signals import user_signed_up
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(user_signed_up)
def create_profile(request, user, **kwargs):
    """ Listens to the allauth user_signed_up signal to automatically create a profile upon successful authentication """
    # Source: (Allauth) https://github.com/pennersr/django-allauth/blob/master/allauth/account/signals.py
    # Source: (Stackoverflow example) https://stackoverflow.com/questions/40684838/django-django-allauth-save-extra-data-from-social-login-in-signal

    userAllauth: User = user
    profile: Profile = Profile.objects.create(user=userAllauth)
    
    profile.full_name = userAllauth.get_full_name()
    profile.email = userAllauth.email

    # Profile is a foreign key in the User model
    userAllauth.profile.save()


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def save_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile1 = Profile(user=user)
        profile1.save()