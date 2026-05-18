from django.test import TestCase
from django.test.utils import override_settings
from django.urls import reverse


class TestHandlers(TestCase):

    def test_400(self):
        self.client.raise_request_exception = False
        response = self.client.get(reverse("error_400"))
        self.assertEqual(400, response.status_code)
        self.assertIn(
            "<title>Requête incorrecte - EPFL</title>",
            response.content.decode(),
        )
        self.assertTemplateUsed(response, "web2018/includes/400-fr.html")

    def test_403(self):
        response = self.client.get(reverse("error_403"))
        self.assertEqual(403, response.status_code)
        self.assertIn(
            "<title>Accès interdit - EPFL</title>", response.content.decode()
        )
        self.assertTemplateUsed(response, "web2018/includes/403-fr.html")

    def test_404(self):
        response = self.client.get("/foobar")
        self.assertEqual(404, response.status_code)
        self.assertIn(
            "<title>Page non trouvée - EPFL</title>", response.content.decode()
        )
        self.assertTemplateUsed(response, "web2018/includes/404-fr.html")

    @override_settings(LANGUAGE_CODE="es")
    def test_404_with_unknown(self):
        response = self.client.get("/foobar")
        self.assertEqual(404, response.status_code)
        self.assertIn(
            "<title>Page not found - EPFL</title>", response.content.decode()
        )
        self.assertTemplateUsed(response, "web2018/includes/404-en.html")

    def test_500(self):
        self.client.raise_request_exception = False
        response = self.client.get(reverse("error_500"))
        self.assertEqual(500, response.status_code)
        self.assertIn(
            "<title>Erreur interne du serveur - EPFL</title>",
            response.content.decode(),
        )
        self.assertTemplateUsed(response, "web2018/includes/500-fr.html")
