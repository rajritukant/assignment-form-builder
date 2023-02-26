from backend.models import SourceFormTemplate
from backend.serializers.source_form_templates_serializer import SourceFormTemplatesSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..schemas import source_form_template_schema
from jsonschema import validate
from django.db import transaction
from rest_framework import generics


# class SourceFormTemplateList(generics.ListCreateAPIView):
#     """
#     List all source form templates, or create a new template
#     """
#     queryset = SourceFormTemplate.objects.all()
#     serializer_class = SourceFormTemplatesSerializer
#


class SourceFormTemplateList(APIView):
    """
    List all source form templates, or create a new template
    """
    def get(self, request, format=None):
        source_form_templates = SourceFormTemplate.objects.all()
        serializer = SourceFormTemplatesSerializer(source_form_templates, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # validate schema using jsonschema and then create db entries for the source template
        validate(instance=request.data, schema=source_form_template_schema)
        schema_data = {
            'type': request.data.get('type'),
            'schema': request.data
        }
        fields_data = request.data.get('fields')

        with transaction.atomic():
            serializer = SourceFormTemplatesSerializer(data=schema_data)
            if serializer.is_valid():
                source_form_obj = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SourceFormTemplateDetail(APIView):
    """
    Retrieve, a source form template.
    """
    def get_object(self, source_type):
        try:
            return SourceFormTemplate.objects.get(type=source_type)
        except SourceFormTemplate.DoesNotExist:
            raise Http404

    def get(self, request, source_type, format=None):
        snippet = self.get_object(source_type)
        serializer = SourceFormTemplatesSerializer(snippet)
        return Response(serializer.data)

