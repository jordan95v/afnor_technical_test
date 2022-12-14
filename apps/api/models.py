from django.db import models

# Create your models here.

__all__: list[str] = ["Standard', 'Support"]


class Standard(models.Model):
    numdos: models.CharField = models.CharField(max_length=8, unique=True)
    numdos_vl: models.CharField = models.CharField(max_length=8, null=True, blank=True)
    ancart: models.CharField = models.CharField(max_length=25, null=True, blank=True)
    channel: models.CharField = models.CharField(max_length=3, null=True, blank=True)
    stage: models.FloatField = models.FloatField(null=True, blank=True)
    ve: models.CharField = models.CharField(max_length=3, null=True, blank=True)


class Support(models.Model):
    standard: models.ForeignKey = models.ForeignKey(
        Standard, on_delete=models.CASCADE, related_name="support"
    )
    format: models.CharField = models.CharField(max_length=5, null=True, blank=True)
