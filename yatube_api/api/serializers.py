from posts.models import Comment, Group, Post, User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True, required=False)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('author', 'post')

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        comment = Comment.objects.create(**validated_data)
        return comment


class PostSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(slug_field='id',
                                         queryset=Group.objects.all(),
                                         allow_null=True,
                                         required=False)
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = (
            'id', 'text', 'author', 'image', 'group', 'pub_date'
        )

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        post = Post.objects.create(**validated_data)
        return post


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')
