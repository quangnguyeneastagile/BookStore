from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

import time
import factory

from .factories import *
from .models import *

class MySeleniumTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super(MySeleniumTests, cls).setUpClass()
        cls.selenium = WebDriver()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(MySeleniumTests, cls).tearDownClass()

    def create_db(self):
        for i in range(1,10):
            BookFactory(title = factory.Faker('sentence',nb_words=4),
                        author = AuthorFactory(name = factory.Faker('name')),
                        category = CategoryFactory(name = factory.Faker('word'))
            )
        pass

    def test_author(self):
        #create 10 books
        self.create_db()
        self.selenium.get('%s%s' % (self.live_server_url, '/catalog/'))
        time.sleep(20)
        #import pdb; pdb.set_trace

        #self.selenium.get('%s%s' % (self.live_server_url, '/catalog/'))
        #import pdb; pdb.set_trace()
        #time.sleep(180)
        #author_name_input = self.selenium.find_element_by_name('author_name')
        #author_name_input.send_keys('Hugo CDE')
        #self.selenium.find_element_by_xpath('//input[@value="OK"]').click()
