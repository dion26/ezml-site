from dataclasses import field
from rest_framework import serializers

from .models import Thread, LikeThread
from base.serializers import UserPublicSerializer

class LikeThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeThread
        fields = ['users']
        read_only_fields = ['thread']


class ThreadSerializer(serializers.HyperlinkedModelSerializer):
    user_upvote = serializers.SerializerMethodField()
    user_downvote = serializers.SerializerMethodField()
    host = UserPublicSerializer(read_only=True)
    topics = serializers.CharField(source='subforum.name', read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='thread',
        lookup_field='slug'
    )
    likes = LikeThreadSerializer()
    class Meta:
        model = Thread
        fields = [
            'id',
            'host',
            'user_upvote',
            'user_downvote',
            'sticked',
            'topics',
            'name',
            'text_fill',
            'total_comments',
            'url',
            'likes',
            'posted_since',
            'get_top_score',
            'get_hot_score',
            'slug',
        ]
        read_only_fields = ['text_fill', 'name', 'sticked']

    def get_user_upvote(self, obj):
        log_in_user = self.context['request'].user
        upvote_users = obj.likes.users
        is_upvoting = upvote_users.filter(id=log_in_user.id).exists()
        return is_upvoting

    def get_user_downvote(self, obj):
        log_in_user = self.context['request'].user
        downvote_users = obj.dis_likes.users
        is_downvoting = downvote_users.filter(id=log_in_user.id).exists()
        return is_downvoting