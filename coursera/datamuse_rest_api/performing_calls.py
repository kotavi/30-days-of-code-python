from coursera.datamuse_rest_api.rest.datamuse import *


response = get_words_with_similar_meaning("healthy")
if response.status_code != 200:
    raise Exception('Cannot execute get request: {}'.format(response.status_code))
print('Response: {}'.format(response.json()))

response = get_words_by_regex("h?????y")
if response.status_code != 200:
    raise Exception('Cannot execute get request: {}'.format(response.status_code))
print('Response: {}'.format(response.json()))


response = get_words_spelled_similarly("kitten")
if response.status_code != 200:
    raise Exception('Cannot execute get request: {}'.format(response.status_code))
print('Response: {}'.format(response.json()))