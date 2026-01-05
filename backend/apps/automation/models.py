from django.db import models
from core.base_models import TimeStampedModel

class Workflow(TimeStampedModel):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'workflows'
