from django.db import models


class SourceFormTemplate(models.Model):
    id = models.AutoField(primary_key=True, editable=False)

    type = models.CharField(default=None, null=False, blank=False, max_length=255, unique=True, db_index=True)
    schema = models.JSONField(default=None)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __unicode__(self):
        return str(self.type)

    def __repr__(self):
        return str(self.type)

    def __str__(self):
        return str(self.type)

    class Meta:
        db_table = "source_form_template"
        app_label = "backend"
