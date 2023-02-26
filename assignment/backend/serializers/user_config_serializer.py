from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from backend.models import UserConfig, SourceFormTemplate
from backend.validators import validate_regex


class UserConfigSerializer(serializers.Serializer):
    # user_config = serializers.PrimaryKeyRelatedField(queryset=UserConfig.objects.all())
    id = serializers.IntegerField(read_only=True)
    apiKey = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    category = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    useHTTP = serializers.BooleanField(default=None, allow_null=True)
    source = serializers.CharField(max_length=255, allow_null=False, allow_blank=False)

    # def validate_source_type(self, source_type_value):
    #     try:
    #         source_form_template = SourceFormTemplate.objects.get(type=source_type_value)
    #     except SourceFormTemplate.DoesNotExist:
    #         raise ValidationError("invalid source_type")
    def create(self, validated_data):
        try:
            validated_data['source'] = SourceFormTemplate.objects.get(type=validated_data['source'])
        except SourceFormTemplate.DoesNotExist:
            raise serializers.ValidationError('invalid source')
        # now we have source form template instance.
        source_form_template_schema = validated_data.get('source').schema

        # now check that apiKey, useHTTP and category are valid
        self.validate_user_config_with_schema(source_form_template_schema, validated_data)

        return UserConfig.objects.create(**validated_data)

    def validate_api_key_with_schema(self, api_key_schema, serializer_validated_data):
        if api_key_schema.get('required'):
            # api key is required
            # check user input for api key
            if not serializer_validated_data.get('apiKey', None):
                raise ValidationError("apiKey is required")
            # validate against regex, raise regex error message
            validate_regex(serializer_validated_data.get('apiKey'), api_key_schema.get('regex'),
                           api_key_schema.get('regexErrorMessage'))

    def validate_use_http_with_schema(self, use_http_schema, serializer_validated_data):
        if use_http_schema.get('required'):
            if not serializer_validated_data.get('useHTTP', None):
                raise ValidationError("useHTTP is required")

    def validate_category_with_schema(self, category_schema, serializer_validated_data):
        if category_schema.get('required'):
            if not serializer_validated_data.get('category', None):
                raise ValidationError("category is required")
            # check category has a valid value
            valid_values = []
            options = category_schema.get('options')
            for option in options:
                value = option.get("value")
                valid_values.append(value)
            if serializer_validated_data.get('category') not in valid_values:
                raise ValidationError("invalid category")

    def validate_user_config_with_schema(self, source_form_template_schema, serializer_validated_data):
        # validations
        schema_fields = source_form_template_schema.get('fields')
        # validate user input with apikey
        api_key_schema = schema_fields.get('apiKey')
        self.validate_api_key_with_schema(api_key_schema, serializer_validated_data)

        use_http_schema = schema_fields.get('useHTTP')
        self.validate_use_http_with_schema(use_http_schema, serializer_validated_data)

        category_schema = schema_fields.get('category')
        self.validate_category_with_schema(category_schema, serializer_validated_data)




    # def validate_source_form_template(self, source_form_template_id):
    #     return SourceFormTemplate.objects.get(id=source_form_template_id)
    #
