from rest_framework import serializers
from backend.models import SourceFormTemplate


class SourceFormTemplatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = SourceFormTemplate
        fields = ['id',
                  'type',
                  'schema'
                  ]

