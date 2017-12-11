from django.test import TestCase
from django.urls import resolve
from catalog.views import *

class HomePageTest(TestCase):
    #def setUp(self):
        #self.browser = webdriver.Firefox()

    #def tearDown(self):
        #self.browser.quit()

    def test_title_equal_to_expected_homepage_title(self):
        #self.browser.get('http://127.0.0.1:8000/')
        #self.assertIn('To-Do', self.browser.title)
        #self.fail('Finish Check Homepage Title Test!')

        # check that url after resolved, will lead browser to function catalog in views
        found = resolve('/catalog/')
        self.assertEqual(found.func, catalog)


#if __name__ == '__main__':
#    unittest.main(warnings='ignore')
