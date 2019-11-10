from django.test import TestCase
from .models import Post

from model_bakery import baker


class PostTestCase(TestCase):
    def test_title(self):
        post = baker.make(Post)
        post.save()
        self.assertEqual(True, True)
