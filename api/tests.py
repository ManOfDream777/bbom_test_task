from django.contrib.auth import authenticate
from rest_framework.test import APIClient, APITestCase
from rest_framework.reverse import reverse

from main.models import MyUser, Post


class APITest(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user: MyUser = MyUser.objects.create_user(
            username='Nikita',
            email='nikita@gmail.com',
            password='dioaw212doawd'
        )

    def test_all_users(self):
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
        data = {
            'username': 'nikita',
            'email': 'nikitka@gmail.com',
            'password': 'odiajwdi2'
        }
        url = reverse('api:sign_up')
        response = self.client.post(url, data=data)
        assert response.status_code == 302

    def test_sign_up_user_exists(self):
        """ Must return 400 """
        data = {
            'username': self.user.username,
            'email': 'nikitka@gmail.com',
            'password': 'odiajwdi2'
        }
        url = reverse('api:sign_up')
        response = self.client.post(url, data=data)
        assert response.status_code == 400

    def test_login(self):
        data = {
            'username': self.user.username,
            'password': 'dioaw212doawd'
        }
        url = reverse('api:sign_in')
        response = self.client.post(url, data=data)
        assert response.status_code == 302

    def test_login_invalid(self):
        """ Must return 401 """
        data = {
            'username': self.user.username,
            'password': 'some password'
        }
        url = reverse('api:sign_in')
        response = self.client.post(url, data=data)
        assert response.status_code == 401

