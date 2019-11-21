import unittest

from coursera.datamuse_rest_api.rest.datamuse import *


class Datamuse(unittest.TestCase):

    def test_words_with_similar_meaning(self):
        response = get_words_with_similar_meaning("healthy")
        self.assertEqual(response.status_code, 200, 'Cannot execute get request: {}'.format(response.status_code))
        self.assertTrue('good' == response.json()[0]['word'], 'Cannot execute get request: {}'.format(response.status_code))

    def test_words_by_regex(self):
        response = get_words_by_regex("h?????y")
        self.assertEqual(response.status_code, 200, 'Cannot execute get request: {}'.format(response.status_code))
        words_list = [data['word'] for data in response.json()]
        for word in words_list:
            self.assertTrue(word[0] == 'h' and word[-1] == 'y', 'Cannot execute get request: {}'.format(response.status_code))

    def test_words_spelled_similarly(self):
        response = get_words_spelled_similarly("kitten")
        words_list = [data['word'] for data in response.json()]
        self.assertEqual(response.status_code, 200, 'Cannot execute get request: {}'.format(response.status_code))
        self.assertTrue('mitten' in words_list, 'Cannot execute get request: {}'.format(response.status_code))


if __name__ == '__main__':
    unittest.main()
