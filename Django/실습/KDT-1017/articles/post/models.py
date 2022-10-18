from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', 
        blank=True)
    thumbnail = ProcessedImageField(
        upload_to='images/', 
        blank=True,
        processors=[Thumbnail(400, 300)],
        format='JPEG',
        options={'quality': 80},
        )
