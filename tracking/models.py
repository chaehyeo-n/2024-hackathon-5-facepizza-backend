from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def HighlightImage_upload_path(instance, filename):
    return f'{instance.pk}/{filename}'

EMOTION_CHOICES = [
    ('happy', '행복'),
    ('sad', '슬픔'),
    ('angry', '분노'),
    ('surprised', '놀람'),
    ('disgusted', '혐오'),
    ('fearful', '두려움'),
    ('neutral', '무표정'),
]

class Report(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, blank=False, on_delete=models.CASCADE)
    happy = models.FloatField(default=0)
    sad = models.FloatField(default=0)
    angry = models.FloatField(default=0)
    surprised = models.FloatField(default=0)
    disgusted = models.FloatField(default=0)
    fearful = models.FloatField(default=0)
    neutral = models.FloatField(default=0)

    created_at = models.DateTimeField()
    ended_at = models.DateTimeField()
    title = models.CharField(max_length=50, null=True)

    happy_highlight = models.TextField(blank=True)
    sad_highlight = models.TextField(blank=True)
    angry_highlight = models.TextField(blank=True)
    surprised_highlight = models.TextField(blank=True)
    disgusted_highlight = models.TextField(blank=True)
    fearful_highlight = models.TextField(blank=True)
    neutral_highlight = models.TextField(blank=True)

    happy_maxValue = models.FloatField(default=0)
    sad_maxValue = models.FloatField(default=0)
    angry_maxValue = models.FloatField(default=0)
    surprised_maxValue = models.FloatField(default=0)
    disgusted_maxValue = models.FloatField(default=0)
    fearful_maxValue = models.FloatField(default=0)
    neutral_maxValue = models.FloatField(default=0)