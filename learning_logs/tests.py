import datetime

from django.test import TestCase

from .models import Topic, Entry

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
