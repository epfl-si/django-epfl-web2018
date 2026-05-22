from django.test import TestCase


class TestTemplates(TestCase):

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(200, response.status_code)
        self.assertIn(
            "<title>Test Home - EPFL</title>",
            response.content.decode(),
        )
        self.assertIn(
            "Test App",
            response.content.decode(),
        )
        self.assertIn(
            "About",
            response.content.decode(),
        )
