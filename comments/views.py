from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves comments
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (AllowAny,)

    @action(detail=True, methods=['GET', 'POST'])
    def replys(self, request, pk=None):
        qs = self.get_queryset().get(id=pk)
        data = self.serializer_class(qs, many=False).data
        return Response(data)