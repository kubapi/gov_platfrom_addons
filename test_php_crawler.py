import unittest
#importing specfic function
from php_crawler import crawl_words

class TestPhpCrawler(unittest.TestCase):

    def setUp(self):
        #using external text data similar to the ones found in repo
        self.file = open("test_data.php", encoding='utf-8', mode='r')

    def test_multiple_tags(self):
        text = '<><><><><a>OO</a><<<>>>>'
        result = crawl_words(text)
        self.assertEqual(result, '>OO<')

    #specific for the way world_crawl works
    def test_stoping_point(self):
        text = '<div class="xyz">O, O. O; O/ </div>'
        result = crawl_words(text)
        self.assertEqual(result, '>O, O. O; O/ <')

    def test_with_href_php(self):
        text = "<a href='<?php echo base_url('postepowania')?>' class='btn btn-outline-secondary btn-block''>OOO</a>"
        result = crawl_words(text)
        self.assertEqual(result, '>OOO<')

    def test_empty(self):
        text = '<a href="<?php echo base_url("postepowania")?>"><a/>'
        result = crawl_words(text)
        self.assertFalse(result)

    def test_multiple_findings(self):
        result = len(crawl_words(self.file))
        self.assertGreater(result, 5)

if __name__ == '__main__':
    unittest.main()
