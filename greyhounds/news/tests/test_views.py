from django.test import TestCase
from model_mommy import mommy
from news.models import Tag, News
from news.views import index

class TestIndex(TestCase):
    
    def test_multiple_tags_return_distinct_newsitems(self):
        tag1 = mommy.make(Tag)
        tag2 = mommy.make(Tag)
        news_item = mommy.make(News, tags=[tag1, tag2])
        resp = self.client.get("/news/?tags=%s,%s" % (tag1.name, tag2.name))
        # Must only return 1 News item
        self.assertEqual(len(resp.context["news"]), 1)
        