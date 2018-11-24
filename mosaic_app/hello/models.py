from django.db import models
from django.core.exceptions import ValidationError


def validate_image(image):

    file_size = image.file.size

    # 500KB以下許容
    max_kb = 500
    if file_size > max_kb * 1024:
        raise ValidationError("Max size of file is %s KB" % max_kb)

    # 1KB以上許容
    min_kb = 1
    if file_size < min_kb * 1024:
        raise ValidationError("Min size of file is %s KB" % min_kb)


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='gallery/', blank=False, validators=[validate_image])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    gray = models.ImageField(upload_to='gray/', default='Not Set')
    mosaic = models.ImageField(upload_to='gray/', default='Not Set')
