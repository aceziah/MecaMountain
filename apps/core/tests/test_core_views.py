from django.test import TestCase
from django.urls import reverse
from django.core import mail


class CoreViewsTests(TestCase):

    def test_home_page(self):
        response = self.client.get(reverse("core:home"))

        self.assertEqual(response.status_code, 200)

    def test_contact_page(self):
        response = self.client.get(reverse("core:contact"))

        self.assertEqual(response.status_code, 200)

    def test_privacy_page(self):
        response = self.client.get(reverse("core:privacy"))

        self.assertEqual(response.status_code, 200)

    def test_contact_form_sends_email(self):
        data = {
            "name": "Jean Dupont",
            "email": "jean@example.com",
            "subject": "Projet électronique",
            "message": "Bonjour, je souhaiterais échanger avec vous.",
        }

        response = self.client.post(
            reverse("core:contact"),
            data,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 1)

        email = mail.outbox[0]

        self.assertEqual(
            email.subject,
            "[MecaMountain] Projet électronique",
        )

        self.assertIn("Jean Dupont", email.body)
        self.assertIn("jean@example.com", email.body)
        self.assertIn(
            "Bonjour, je souhaiterais échanger avec vous.",
            email.body,
        )

        self.assertEqual(
            email.reply_to,
            ["jean@example.com"],
        )

    def test_contact_form_invalid_does_not_send_email(self):
        data = {
            "name": "",
            "email": "email-invalide",
            "subject": "",
            "message": "",
        }

        response = self.client.post(
            reverse("core:contact"),
            data,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 0)