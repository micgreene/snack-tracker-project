from django.test import SimpleTestCase
from django.urls import reverse

class SnacksTests(SimpleTestCase):
  def test_home_page_status_code(self):
    url = reverse('snack_list')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_home_base_template(self):
    url = reverse('snack_list')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'base.html')