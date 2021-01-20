from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def list(self, request, *args, **kwargs):
        return Response([])

    @action(detail=False, methods=['GET'])
    def mentionable(self, *args, **kwargs):
        qs = self.get_queryset().filter(is_staff=False)
        data = self.serializer_class(qs, many=True).data
        return Response(data)
