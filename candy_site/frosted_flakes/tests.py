from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class FrostedTests(SimpleTestCase):

    def test_frosted_flakes_page_status(self):
        url = reverse('frosted_flakes')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_templates_used(self):
        url = reverse('frosted_flakes')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'frosted-flakes-home.html')
        self.assertTemplateUsed(response, 'nav.html')