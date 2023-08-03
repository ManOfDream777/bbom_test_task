from django.urls import path
from .views import Home, Posts

app_name = 'main'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('posts/<int:id>', Posts.as_view(), name='posts'),
]