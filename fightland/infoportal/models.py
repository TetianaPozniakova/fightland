from django.db import models

class Video(models.Model):
    video_title = models.CharField(max_length = 150)
    video_id = models.CharField(max_length = 50)
    date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.video_title
