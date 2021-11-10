from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(max_length=800)
    author_name = models.CharField(max_length=255)
    upvote_amount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def add_upvote(self):
        self.upvote_amount += 1
        self.save()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=800)
    author_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
