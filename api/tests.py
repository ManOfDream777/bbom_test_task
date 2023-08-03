from django.contrib.auth import authenticate
from rest_framework.test import APIClient, APITestCase
from rest_framework.reverse import reverse

from main.models import MyUser, Post


class APITest(APITestCase):
    """ API Testing """

    def setUp(self) -> None:
        self.client = APIClient()
        self.user: MyUser = MyUser.objects.create_user(
            username='Nikita',
            email='nikita@gmail.com',
            password='dioaw212doawd'
        )

    def test_all_users(self):
        """ Тест для отображения всех пользователей в системе """
        MyUser.objects.create(
            username='Alina',
            email='alina@gmail.com',
            password='dioawdoawd'
        )

        url = reverse('api:all_users')

        response = self.client.get(url)

        assert len(response.json()) == 2
        assert response.status_code == 200

    def test_all_posts_of_user(self):
        """ Тест для отображения постов конкретного пользователя """

        # Создание другого пользователя, чтобы привязать к нему пост
        another_user = MyUser.objects.create(
            username='Alina',
            email='alina@gmail.com',
            password='dioawdoawd'
        )

        Post.objects.create(
            title='Test',
            body='test body',
            user=self.user
        )

        Post.objects.create(
            title='Test2',
            body='test body2',
            user=self.user
        )

        #Создание поста не относящегося к постам проверяемого пользователя
        Post.objects.create(
            title='Test3',
            body='test body3',
            user=another_user
        )

        url = reverse('api:posts_of_user')
        self.client.force_login(self.user)
        response = self.client.get(url)

        assert response.status_code == 200
        assert len(response.json()) == 2

    def test_creation_post(self):
        """ Тест для проверки создания поста """
        data = {
            'title': 'test',
            'body': 'body',
        }
        self.client.force_login(self.user)

        url = reverse('api:add_post')
        response = self.client.post(url, data=data)

        assert response.status_code == 201
        assert Post.objects.count() == 1

    def test_delete_post(self):
        """ Тест для проверки удаления поста """
        post = Post.objects.create(
            title='Test',
            body='test body',
            user=self.user
        )
        self.client.force_login(self.user)
        url = reverse('api:delete_post', kwargs={'id': post.id})
        response = self.client.delete(url)
        assert response.status_code == 204

    def test_sign_up(self):
        """ Тест для проверки регистрации """
        data = {
            'username': 'nikita',
            'email': 'nikitka@gmail.com',
            'password': 'odiajwdi2'
        }
        url = reverse('api:sign_up')
        response = self.client.post(url, data=data)
        assert response.status_code == 302

    def test_sign_up_user_exists(self):
        """ Тест для проверки работоспособности регистрации, если пользователь уже зарегистрирован в системе """
        data = {
            'username': self.user.username,
            'email': 'nikitka@gmail.com',
            'password': 'odiajwdi2'
        }
        url = reverse('api:sign_up')
        response = self.client.post(url, data=data)
        assert response.status_code == 400

    def test_login(self):
        """ Тест для проверки работоспособности авторизации """ 
        data = {
            'username': self.user.username,
            'password': 'dioaw212doawd'
        }
        url = reverse('api:sign_in')
        response = self.client.post(url, data=data)
        assert response.status_code == 302

    def test_login_invalid(self):
        """ Тест для проверки работоспособности авторизации, если данные не верны """ 

        data = {
            'username': self.user.username,
            'password': 'some password'
        }
        url = reverse('api:sign_in')
        response = self.client.post(url, data=data)
        assert response.status_code == 401

