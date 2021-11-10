from django.urls import path, include

from posts.views import PostListCreateView

app_name = 'posts'

urlpatterns = [
    path('', PostListCreateView.as_view(), name='post-list-create'),
]

