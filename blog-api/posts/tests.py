from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


class PostModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        
        test_user1 = User.objects.create_user(username="test_user1", password="abc123")
        test_user1.save()

        test_post = Post.objects.create(author=test_user1, title="Blog Title", body="Body content...")
        test_post.save()

    def test_post_content(self):

        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'

        self.assertEqual(author, 'test_user1')
        self.assertEqual(title, 'Blog Title')
        self.assertEqual(body, 'Body content...')
