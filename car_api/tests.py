from _typeshed import Self
from django import test
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Car

# Create your tests here.
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()
        test_post = Car.objects.create(title='Test Post Body', author=testuser1)
        test_post.save()

    def test_blog_content(self):
        post = Car.objects.get(id = 1)
        expected_auther = f'{post.auther}'
        expected_title = f'{post.title}'
        expected_body = f'{post.body}'
        self.assertEqual(expected_auther, 'testuser1')
        self.assertEqual(expected_title, 'Test Post')
        self.assertEqual(expected_body, 'Test Post Body')