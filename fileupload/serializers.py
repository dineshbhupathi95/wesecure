from rest_framework.serializers import ModelSerializer
from . models import *
from rest_framework import serializers
class fileuploadserializer(ModelSerializer):
    class Meta:
        model = Files
        fields = "__all__"

class getFileSerializer(ModelSerializer):
    plugin_name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    risk_factor = serializers.SerializerMethodField()

    def get_plugin_name(self, obj):
        print(obj[0])
        return '{}'.format(obj[0])

    def get_description(self, obj):
        return '{}'.format(obj[1])

    def get_risk_factor(self, obj):
        return '{}'.format(obj[2])
    class Meta:
        model = Files
        fields = ["plugin_name","description","risk_factor"]