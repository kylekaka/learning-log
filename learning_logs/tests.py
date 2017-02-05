import datetime
import unittest

from django.test import Client
from django.test import TestCase

from .models import Topic, Entry

class SimpleTest(unittest.TestCase):
    def test_index(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        client = Client()
        response = client.get('/users/login')
        self.assertEqual(response.status_code, 200)


# 单元测试代码
class TopicMethodTests(TestCase):
    """
    主题的单元测试
    """
    def test_topic_name(self):
        id_last = len(Topic.objects.all())
        #self.assertEqual(id_last, 'test-topic')
        t = Topic.objects.get(id=1)
        self.assertEqual(t.text, 'test-topic')

class EntryMethodTests(TestCase):
    """
    条目的单元测试
    """
    def test_entry_name(self):
        id_last = len(Entry.objects.all())
        e = Entry.objects.get(id=id_last)
        self.assertIs(e.text, 'test-topic')
