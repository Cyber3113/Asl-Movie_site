from django.db import models

class Video_type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Video(models.Model):
    image = models.ImageField(upload_to="image/")
    name = models.CharField(max_length=50)
    video_file = models.FileField(upload_to="videos/")
    type = models.ForeignKey(Video_type, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    
