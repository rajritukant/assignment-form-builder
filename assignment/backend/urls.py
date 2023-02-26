from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .views.source_form_templates_view import SourceFormTemplateList, SourceFormTemplateDetail
from .views.user_config_view import UserConfigList

urlpatterns = [
    path("test/", views.test_func, name="test"),
    path("source-form-templates/", SourceFormTemplateList.as_view()),
    path("source-form-templates/<slug:source_type>/", SourceFormTemplateDetail.as_view()),
    path('config/', UserConfigList.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
