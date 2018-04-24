from django.db import models

# Create your models here.


class Email(models.Model):
    slug = models.CharField(max_length=32)
    email = models.EmailField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('slug', 'email')
