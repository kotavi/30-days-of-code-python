import unittest

from coursera.datamuse_rest_api.rest.datamuse import *


class Datamuse(unittest.TestCase):

    def test_sum(self):
        response = get_words_with_similar_meaning("healthy")
        print(response.json()[0]['word'])
        self.assertEqual(response.status_code, 200, 'Cannot execute get request: {}'.format(response.status_code))
        self.assertTrue('good' == response.json()[0]['word'], 'Cannot execute get request: {}'.format(response.status_code))


if __name__ == '__main__':
    unittest.main()
