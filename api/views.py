from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .serializers import ListOfUserSerializer, ListOfUserPostsSerializer, AddPostSerializer, SignUpSerializer, SignInSerializer
from main.models import MyUser, Post

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse


class AllUsersAPIView(ListAPIView):
    """ View для отображения всех пользователей в системе """

    serializer_class = ListOfUserSerializer
    queryset = MyUser.objects.all()


class ListOfPostsAPIView(ListAPIView):
    """ View для отображения всех постов пользователя """

    serializer_class = ListOfUserPostsSerializer
    queryset = Post.objects.none()

    def get(self, request, *args, **kwargs):
        self.queryset = Post.objects.filter(user=self.request.user)
        return super().get(request, *args, **kwargs)


class CreatePostAPIView(CreateAPIView):
    """ View для создания поста """

    serializer_class = AddPostSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response(status=201)


class DeletePostAPIView(DestroyAPIView):
    """ View для удаления поста """

    permission_classes = (IsAuthenticated, )
    lookup_field = 'id'
    queryset = Post.objects.none()

    def destroy(self, request: Request, *args, **kwargs):
        self.queryset = Post.objects.filter(user=request.user)
        return super().destroy(request, *args, **kwargs)


class SignUpAPIView(CreateAPIView):
    """ View для обработки регистрации """
    serializer_class = SignUpSerializer
    queryset = MyUser.objects.none()

    def get(self, request: Request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('main:home'))
        return Response(status=405)

    def post(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        MyUser.objects.create_user(
            username=serializer.validated_data.get('username'),
            email=serializer.validated_data.get('email'),
            password=serializer.validated_data.get('password'))

        user = authenticate(request, username=serializer.validated_data.get(
            'username'), password=serializer.validated_data.get('password'))
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('main:home'))
        return Response(status=401)


class SignInAPIView(APIView):
    """ View для обработки авторизации """

    def post(self, request: Request, *args, **kwargs):
        serializer = SignInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(request, username=serializer.validated_data.get(
            'username'), password=serializer.validated_data.get('password'))
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('main:home'))
        return Response(status=401)

    def get(self, request: Request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('main:home'))
        return Response(status=405)
