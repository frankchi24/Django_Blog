from django.test import TestCase
from .models import Post
from django.contrib.auth import get_user_model
# Create your tests here.

User = get_user_model()

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(
        user = User.objects.first(),
        title = 'Some Title',
        subtitle = 'Some Subtitle',
        content = 'Some Content Bla Bla Bla...'
        )
    def test_post_item(self):
        obj = Post.objects.create(
            user = User.objects.first(),
            title = 'Some Title',
            subtitle = 'Some Subtitle',
            content = 'Some Content Bla Bla Bla...'
        )
        self.assetTrue(
            obj.user == 'admin',
            obj.title == 'Some Title',
            obj.subtitle == 'Some Subtitle',
            obj.content == 'Some Content Bla Bla Bla...',
        )
