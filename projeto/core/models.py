from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        "Criado em",
        auto_now_add=True,
        auto_now=False
    )
    modifield = models.DataTimeField(
        'modificado em',
        auto_now_add=False,
        auto_now=True 
    )

    class Meta:
        abstract = True