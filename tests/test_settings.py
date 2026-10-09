from django.conf import settings
from django.test import RequestFactory, TestCase
from django.test.utils import override_settings

from django_epfl_web2018.context_processors import web2018_settings
from django_epfl_web2018.core import get_web2018_setting


class TestSettings(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    @override_settings(WEB2018={"SHOW_BREADCRUMB": False, "OTHER": "value"})
    def test_settings_when_configured(self):
        context = web2018_settings(self.factory.get("/"))
        self.assertEqual(
            {
                "web2018_settings": {
                    "SHOW_BREADCRUMB": False,
                    "SITE_TITLE_SUFFIX": "EPFL",
                    "OTHER": "value",
                }
            },
            context,
        )

    def test_settings_not_defined(self):
        with override_settings():
            del settings.WEB2018
            context = web2018_settings(self.factory.get("/"))
            self.assertEqual(
                {
                    "web2018_settings": {
                        "SHOW_BREADCRUMB": True,
                        "SITE_TITLE_SUFFIX": "EPFL",
                    }
                },
                context,
            )

    @override_settings(WEB2018=None)
    def test_settings_none(self):
        context = web2018_settings(self.factory.get("/"))
        self.assertEqual(
            {
                "web2018_settings": {
                    "SHOW_BREADCRUMB": True,
                    "SITE_TITLE_SUFFIX": "EPFL",
                }
            },
            context,
        )

    @override_settings(WEB2018="invalid")
    def test_settings_is_invalid(self):
        context = web2018_settings(self.factory.get("/"))
        self.assertEqual(
            {
                "web2018_settings": {
                    "SHOW_BREADCRUMB": True,
                    "SITE_TITLE_SUFFIX": "EPFL",
                }
            },
            context,
        )

    @override_settings(WEB2018={})
    def test_settings_is_empty(self):
        context = web2018_settings(self.factory.get("/"))
        self.assertEqual(
            {
                "web2018_settings": {
                    "SHOW_BREADCRUMB": True,
                    "SITE_TITLE_SUFFIX": "EPFL",
                }
            },
            context,
        )

    @override_settings(WEB2018={"OTHER": "value"})
    def test_settings_with_explicit_default(self):
        self.assertFalse(get_web2018_setting("SHOW_BREADCRUMB", False))

    def test_settings_unknown_key(self):
        with override_settings():
            del settings.WEB2018
            self.assertIsNone(get_web2018_setting("UNKNOWN"))
