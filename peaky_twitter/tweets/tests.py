from django.test import TestCase
from tweets.models import Post

from model_bakery import baker


class PostTestCase(TestCase):
    def test_title(self):
        st = baker.make(Post)
        self.assertEqual(True, True)