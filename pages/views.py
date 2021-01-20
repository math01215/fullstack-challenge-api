from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Page
from .serializers import PageSerializer
from comments.serializers import CommentSerializer


class PageViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves pages
    """
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = (AllowAny,)

    @action(detail=True, methods=['GET', 'POST'])
    def comments(self, request, pk=None):
        # try:
        #     print(request.data["title"])

        #     comment_serializer = CommentSerializer(data=request.data)
        #     # if comment_serializer.is_valid():
        #     try:
        #         comment_serializer.save()
        #     except err:
        #         print(err.text)
        # except:
        #     pass

        # request_data = {"page": 1, "parent": 1, "content": "AAA", 'poster': "d8d779714132452f97977700cf2740fe"}
        comment_serializer = CommentSerializer(data=request.data)
        if comment_serializer.is_valid():
            comment_serializer.save()
        else:
            print('error', comment_serializer.errors)

        qs = self.get_queryset().get(id=pk)
        data = self.serializer_class(qs, many=False).data
        return Response(data)

    # @action(detail=True, methods=['POST'])
    # def comments(self, request, pk=None):
    #     qs = self.get_queryset().get(id=pk)
    #     data = self.serializer_class(qs, many=False).data
    #     return Response(data)