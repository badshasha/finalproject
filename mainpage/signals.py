# from django.contrib.auth.admin import User
# from .models import PicProfile
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
#
# @receiver(signal=post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         PicProfile.objects.create(user_profile=instance)
#
#
# @receiver(signal=post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     instance.picprofile.save()
#
#
