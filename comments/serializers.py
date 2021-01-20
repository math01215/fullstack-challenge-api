from .models import Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    def get_replies(self, obj):
        queryset = Comment.objects.filter(parent_id=obj.id)
        serializer = CommentSerializer(queryset, many=True)
        return serializer.data

    class Meta:
        model = Comment
        fields = '__all__'