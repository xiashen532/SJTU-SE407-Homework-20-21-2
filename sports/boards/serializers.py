# 这是序列化文件
from django.db.models import fields
from django.forms.models import model_to_dict
from rest_framework import serializers

from .models import Board, Topic, Post
from .forms import NewTopicForm


class BoardSerializer(serializers.ModelSerializer):
    '''
    Board序列化
    '''
    class Meta:
        model = Board
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
    '''
    Topic序列化
    '''
    replies = serializers.SerializerMethodField()
    last_updated = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = Topic
        fields = ('id', 'subject', 'last_updated', 'board', 'starter', 'views', 'replies')
        
    def get_replies(self, obj):
        return obj.posts.count()


class PostListSerializer(serializers.ModelSerializer):
    '''
    Post序列化
    '''
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = Post
        fields = ('message', 'topic', 'created_at', 'updated_at', 'created_by', 'updated_by')
