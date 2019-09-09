from django.db import models


class Illustration(models.Model):
    image = models.ImageField(upload_to='static/media/myimages', blank=True)
