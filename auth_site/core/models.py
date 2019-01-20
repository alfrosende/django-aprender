from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class OpusUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    es_supervisor = models.BooleanField(verbose_name="Es supervisor", default=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def crear_usuario_opus(sender, instance, created, **kwargs):
    print(sender,"//",instance,"//",created,"//")
    if created:
        custom = OpusUser.objects.create(user=instance)
        print("es??????? ",custom.es_supervisor)
        custom.es_supervisor = False
        custom.save()

'''
@receiver(post_save, sender=User)
def grabar_usuario_opus(sender, instance, **kwargs):
    instance.opususer.save()
'''