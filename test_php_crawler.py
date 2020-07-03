import unittest
#importing specfic function
from php_crawler import crawl_words

class TestPhpCrawler(unittest.TestCase):

    def setUp(self):
        #using external text data similar to the ones found in repo
        file = open("test_data.php", encoding='utf-8', mode='r')

    def test_multiple_tags(self):
        text = '>>>><a>O</a><<<<'
        result = crawl_words(text)
        self.assertEqual(result, 'O')


if __name__ == '__main__':
    unittest.main()
