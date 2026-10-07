from django.conf import settings
from django.test import TestCase
from django.test.utils import override_settings

from django_epfl_web2018.templatetags.web2018 import (
    web2018_should_show_breadcrumb,
)


class TestBreadcrumb(TestCase):

    def test_breadcrumb_setting_not_defined(self):
        with override_settings():
            del settings.WEB2018
            self.assertTrue(web2018_should_show_breadcrumb())

    @override_settings(WEB2018={})
    def test_breadcrumb_setting_empty(self):
        self.assertTrue(web2018_should_show_breadcrumb())

    @override_settings(WEB2018={"SHOW_BREADCRUMB": False})
    def test_breadcrumb_setting_false(self):
        self.assertFalse(web2018_should_show_breadcrumb())

    @override_settings(WEB2018={"SHOW_BREADCRUMB": True})
    def test_breadcrumb_setting_true(self):
        self.assertTrue(web2018_should_show_breadcrumb())

    @override_settings(WEB2018=None)
    def test_breadcrumb_setting_none(self):
        self.assertTrue(web2018_should_show_breadcrumb())

    @override_settings(WEB2018="invalid")
    def test_breadcrumb_setting_invalid(self):
        self.assertTrue(web2018_should_show_breadcrumb())

    def test_breadcrumb_shown_in_template(self):
        response = self.client.get("/")
        self.assertEqual(200, response.status_code)
        self.assertIn(
            "breadcrumb-container",
            response.content.decode(),
        )

    @override_settings(WEB2018={"SHOW_BREADCRUMB": False})
    def test_breadcrumb_hidden_in_template(self):
        response = self.client.get("/")
        self.assertEqual(200, response.status_code)
        self.assertNotIn(
            "breadcrumb-container",
            response.content.decode(),
        )
