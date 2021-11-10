from django.db import IntegrityError

from common.exceptions import ObjectNotFoundException, IntegrityException
from posts.models import Post
import logging


logger = logging.getLogger(__name__)


class PostServices:
    model = Post

    @classmethod
    def get(cls, **filters):
        try:
            return cls.model.objects.get(**filters)
        except cls.model.DoesNotExist as e:
            logger.error('Post with {params} not found'.format(
                params=', '.join(
                    ['{k}:{v}'.format(k=k, v=v) for k, v in filters.items()])))
            raise ObjectNotFoundException(message='Post with {params} not found'.format(
                params=', '.join(
                    ['{k}:{v}'.format(k=k, v=v) for k, v in filters.items()])))

    @classmethod
    def get_queryset(cls, **filters):
        return cls.model.objects.filter(**filters)

    @classmethod
    def create(cls, title: str, link: str, author_name: str):
        try:
            return cls.model.objects.create(title=title, link=link,
                                            author_name=author_name)
        except IntegrityError as e:
            logger.error(f'Error while creating Post. Error: {e.__cause__}')
            raise IntegrityException(f'Error while creating Post.')

    @classmethod
    def update(cls, post: Post, title: str, link: str,
               author_name: str) -> Post:
        try:
            post.title = title
            post.link = link
            post.author_name = author_name
            post.save()
            return post
        except IntegrityError as e:
            logger.error(f'Error while updating post model. Error: {e.__cause__}')
            raise IntegrityException('Error while updating post model.')

    @classmethod
    def delete(cls, post: Post):
        try:
            post.delete()
        except IntegrityError as e:
            logger.error(f'Error while deleting e_learning model. Error: {e.__cause__}')
            raise IntegrityException('Error while deleting e_learning model.')
