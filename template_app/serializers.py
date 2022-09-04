from rest_framework.serializers import ModelSerializer
from .models import Template


class TemplateModelSerializer(ModelSerializer):
    class Meta:
        model= Template
        fields= '__all__'