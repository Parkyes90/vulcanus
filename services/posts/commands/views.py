from rest_framework import viewsets

from .models import Command
from .serializers import CommandListSerializer, CommandSerializer


class CommandViewSet(viewsets.ModelViewSet):
    queryset = Command.objects.all()

    def get_serializer_class(self):
        if self.action in {"list"}:
            return CommandListSerializer
        return CommandSerializer
