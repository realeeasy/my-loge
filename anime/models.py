from django.db import models

class AnimeVideo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_file = models.FileField(upload_to='anime_videos/')
    thumbnail = models.ImageField(upload_to='anime_thumbnails/', blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
# Create your models here.
