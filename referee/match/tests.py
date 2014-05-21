from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from match.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/match/')  
        self.assertEqual(found.func, home_page) 

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        player_name = 'justin'
        request.POST['username'] = player_name
        request.POST['role'] = 'player'
        request.POST['callback'] = 'http://localhost/player1/'

        response = home_page(request)

        self.assertIn(player_name, response.content.decode())