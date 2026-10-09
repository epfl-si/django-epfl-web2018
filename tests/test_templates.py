from django.test import TestCase
from django.test.utils import override_settings


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

    @override_settings(WEB2018={"SHOW_BREADCRUMB": False})
    def test_home_with_settings(self):
        response = self.client.get("/")
        self.assertNotIn(
            "breadcrumb-container",
            response.content.decode(),
        )
