from django.test import TestCase
from django.urls import reverse


class TestMessages(TestCase):

    def test_warning(self):
        response = self.client.get(reverse("warning"))
        self.assertIn(
            "update alert alert-warning alert-dismissible fade show",
            response.content.decode(),
        )
