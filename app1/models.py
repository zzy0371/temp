from django.db import models

# Create your models here.

class MessageInfo(models.Model):
    info = models.CharField(max_length=20)
    img = models.ImageField(upload_to="ads")
    file = models.FileField(upload_to="files")

    def __str__(self):
        return self.info