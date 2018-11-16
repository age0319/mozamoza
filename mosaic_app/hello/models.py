from django.db import models

# Create your models here.


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    # document = models.FileField(upload_to='documents/')
    photo = models.ImageField(upload_to='gallery/', default='SOME STRING')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    gray = models.ImageField(upload_to='gray/', default='Not Set')
    mosaic = models.ImageField(upload_to='gray/', default='Not Set')
