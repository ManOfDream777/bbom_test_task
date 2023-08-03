from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator


class MyUser(AbstractBaseUser, PermissionsMixin, models.Model):
    """ Кастомная модель пользователя. Никаких изменений за исключением отключения некоторых полей, согласно тз. """

    username_validator = UnicodeUsernameValidator()

    last_login = None
    groups = None
    user_permissions = None

    username = models.CharField(verbose_name="Имя пользователя",
                                max_length=150, unique=True, validators=[username_validator])
    email = models.EmailField(verbose_name='Email', unique=True)
    is_staff = models.BooleanField(
        verbose_name='staff status',
        default=False,
        help_text='Designates whether the user can log into this admin site.',
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Post(models.Model):
    """ Модель поста """

    user = models.ForeignKey(
        MyUser, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(verbose_name='Заголовок поста', max_length=128)
    body = models.TextField(verbose_name='Текст поста')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self) -> str:
        return self.title
