from backend.models import UserConfig
from backend.serializers.user_config_serializer import UserConfigSerializer
from rest_framework import generics


class UserConfigList(generics.ListCreateAPIView):
    queryset = UserConfig.objects.all()
    serializer_class = UserConfigSerializer
