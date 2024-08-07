from django.db import models
from django.contrib.auth.models import User
import os
from django.core.files.storage import default_storage
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.

EMOTION_MAP = {
    '행복': 'happy',
    '슬픔': 'sad',
    '분노': 'angry',
    '놀람': 'surprised'
}

def image_upload_path(instance, filename):
    return f'{instance.user.username}/{filename}'

class EmotionImage(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.TextField(blank=True)
    #image = models.ImageField(upload_to=image_upload_path, blank=True, null=True)
    emotion = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.emotion in EMOTION_MAP:
            self.emotion = EMOTION_MAP[self.emotion]
        super().save(*args, **kwargs)