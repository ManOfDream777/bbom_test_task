# Установка и запуск

## Создайте папку core в рабочей директории и запустите команду 
```bash
git clone https://github.com/ManOfDream777/bbom_test_task.git
```

## Создайте виртуальное окружение командой и активируйте его
```bash
python3 -m venv venv_name
```
Linux/Mac
```bash
source venv_name/bin/activate
```
Windows
```bash
venv_name/Scripts/activate
```

## Установите зависимости 
```bash
pip install -r req.txt
```

# Работа с проектом

## Выполните миграции

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

## Создайте суперпользователя
```bash
python manage.py createsuperuser
```
## Запустите проект 
```bash
python manage.py runserver
```

# Тестирование
## Запуск unit-testов 

```bash
python manage.py test
```

## Пользовательский интерфейс

<ol>
    <li>
        Запустите сервер
    </li>
    <li>
        Главная страница - список всех пользователей
    </li>
    <li>
        Нажатие на имя пользователя - откроет всего его посты. Если Вы являетесь автором - появится кнопка удаления поста и форма добавления нового поста
    </li>
</ol>

# API

### Все пользователи

```http
  GET /api/all_users/
```

### Посты пользователя

```http
  GET /api/posts_of_user/
```
### Добавить пост

```http
  POST /api/add_post/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `title` | `string` | **Обязательно**. Заголовок поста |
| `body` | `string` | **Обязательно**. Текст поста |

### Удалить пост. Удалять пост может только автор

```http
  DELETE /api/delete_post/<int:id>/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `string` | **Обязательно**. ID поста, который надо удалить. |

### Регистрация

```http
  POST /api/sign_up/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Обязательно**. Имя пользователя |
| `email` | `string` | **Обязательно**. Email |
| `password` | `string` | **Обязательно**. Пароль |

### Авторизация

```http
  POST /api/sign_in/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Обязательно**. Имя пользователя |
| `password` | `string` | **Обязательно**. Пароль |

# P.S
### Не стал заморачиваться над внешним видом пользовательского интерфейса, так как задание подразумевало проверить другие навыки и знания. Мои работы по frontend части, вы можете посмотреть в моих репозиториях на GitHub.
