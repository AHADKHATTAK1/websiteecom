from django.db import models
from core.base_models import TimeStampedModel

class Store(TimeStampedModel):
    name = models.CharField(max_length=100)
    subdomain = models.SlugField(unique=True)
    domain = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
