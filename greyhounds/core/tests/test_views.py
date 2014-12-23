from django.test import TestCase


class TestUrls(TestCase):
    """
    Tests to determine that all the basic urls are working.
    """
    def test_basic_urls(self):
        for url in ["/", "/cuhh/", "/varsity/", "/history/"]:
            resp = self.client.get(url)
            self.assertEqual(resp.status_code, 200)
            print resp.content