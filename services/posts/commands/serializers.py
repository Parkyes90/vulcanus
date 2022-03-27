from rest_framework import serializers

from .models import Command


class CommandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = ["id", "name"]


class CommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = ["id", "name", "command"]
