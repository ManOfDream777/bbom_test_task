from django.urls import path
from .views import AllUsersAPIView, ListOfPostsAPIView, CreatePostAPIView, DeletePostAPIView, SignUpAPIView, SignInAPIView

app_name = 'api'

urlpatterns = [
    path('all_users/', AllUsersAPIView.as_view(), name='all_users'),
    path('posts_of_user/', ListOfPostsAPIView.as_view(), name='posts_of_user'),
    path('add_post/', CreatePostAPIView.as_view(), name='add_post'),
    path('delete_post/<int:id>/', DeletePostAPIView.as_view(), name='delete_post'),
    path('sign_up/', SignUpAPIView.as_view(), name='sign_up'),
    path('sign_in/', SignInAPIView.as_view(), name='sign_in'),
]
