import unittest
from app.models import Everything

class EverythingTest(unittest.TestCase):
    '''
    Test class to test the behavior of the Everything class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_everything = Everything('bbc news', 'Hello world!', 'A news to test our source', 'https://www.google.io/img/Mountain', 'https://www.google.io/img/Mountain',  '22-02-2021')

    def tearDown(self):
        self.new_source = None

    def test_instance(self):
        self.assertTrue(isinstance(self.new_everything, Everything))

    def test_init_author(self):
        self.assertEqual(self.new_everything.author, 'bbc news')

    def test_init_title(self):
        self.assertEqual(self.new_everything.title, 'Hello World!')

    def test_init_url(self):
        self.assertEqual(self.new_everything.url, 'https://www.google.io/img/Mountain')

    def test_init_urlToImage(self):
        self.assertEqual(self.new_everything.name, 'https://www.google.io/img/Mountain')

    def test_init_counrty(self):
        self.assertEqual(self.new_everything.country, 'UK')

    def test_init_description(self):
        self.assertEqual(self.new_everything.description, 'A news to test our source')

    def test_init_publishedAt(self):
        self.assertEqual(self.new_everything.publishedAt, '22-02-2021')

        
if __name__ == '__main__':
    unittest.main()