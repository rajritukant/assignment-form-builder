from django.db import models
from backend.models import SourceFormTemplate


class UserConfig(models.Model):
    id = models.AutoField(primary_key=True, editable=False)

    apiKey = models.CharField(default=None, null=True, blank=True, max_length=255)
    category = models.CharField(default=None, null=True, blank=True, max_length=255)
    useHTTP = models.BooleanField(default=None, null=True, blank=True)
    source = models.ForeignKey(SourceFormTemplate, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table = "user_config"
        app_label = "backend"
