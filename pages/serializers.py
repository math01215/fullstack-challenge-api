from .models import Page
from comments.models import Comment

from rest_framework import serializers
from comments.serializers import CommentSerializer

class PageSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    def get_comments(self, obj):
        queryset = Comment.objects.filter(page_id=obj.id, parent_id=None)
        serializer = CommentSerializer(queryset, many=True)
        return serializer.data

    class Meta:
        model = Page
        fields = '__all__'