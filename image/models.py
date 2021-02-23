from django.contrib.auth import get_user_model
from django.db import models
from django.core.exceptions import ValidationError

User = get_user_model()


def file_size(value):
    limit = 200 * 1024
    if value.size > limit:
        raise ValidationError('Размер файла не более 200кб.')


class Image(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/%Y/%m/%d/',
                              validators=[file_size])
