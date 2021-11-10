from django.urls import path, include
from posts.views import PostListCreateView, PostDetailsView, CommentCreateView, CommentDetailsView, PostUpvoteView

app_name = 'posts'

urlpatterns = [
    path('', PostListCreateView.as_view(), name='post-list-create'),
    path('<int:pk>/', PostDetailsView.as_view(), name='post-details'),
    path('<int:pk>/upvote/', PostUpvoteView.as_view(), name='post-upvote'),
    path('comments/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/', CommentDetailsView.as_view(), name='comment-details'),
]

