from rest_framework import serializers
from main.models import MyUser, Post


class ListOfUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = '__all__'


class ListOfUserPostsSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = '__all__'


class AddPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'body')


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password')


class SignInSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=256, required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        fields = ('username', 'password')
