from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class SnickerTests(SimpleTestCase):

    def test_home_page_status(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_page_status(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snickers_page_status(self):
        url = reverse('snickers')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_templates_used(self):
        home_url = reverse('home')
        about_url = reverse('about')
        home_response = self.client.get(home_url)
        about_response = self.client.get(about_url)
        self.assertTemplateUsed(home_response, 'home.html')
        self.assertTemplateUsed(home_response, 'nav.html')

        self.assertTemplateUsed(about_response, 'about.html')
        self.assertTemplateUsed(about_response, 'nav.html')

