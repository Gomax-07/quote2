import unittest
from app.models import Sources

class SourceTest(unittest.TestCase):
    '''
    Test class to test the behavior of the source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources('1', 'BBC News', 'https://ww.bbc.co.uk', 'Uk', 'A news to test our source')

    def tearDown(self):
        self.new_source = None
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Sources))

    def test_init_id(self):
        self.assertEqual(self.new_source.id, '1')

    def test_init_name(self):
        self.assertEqual(self.new_source.name, 'BBC News')

    def test_init_url(self):
        self.assertEqual(self.new_source.url, 'https://ww.bbc.co.uk')

    def test_init_county(self):
        self.assertEqual(self.new_source.country, 'UK')

    def test_init_description(self):
        self.assertEqual(self.new_source.description, 'A news to test our source')

if __name__ == '__main__':
    unittest.main()