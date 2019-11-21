import requests
import json

with open('apikey.json', 'r') as f:
    apikey = json.loads(f.read())['apikey']

def get_movies_from_tastedive(name):
    """

    :param name: name of the movie
    :return: dictionary with movies that are similar to the input movie
    """
    params = {"q": name, "type": "movies", "limit": 5}
    base_url = "https://tastedive.com/api/similar"
    result = requests.get(base_url, params=params)
    print("Request was sent to URL: ", result.url)
    print("First 100 symbols in the response: ", result.text[:100])
    return json.loads(result.text)


def extract_movie_titles(dict_):
    """

    :param dict_: dictionary with original and similar movies
    :return: a list of similar movie titles
    """
    lst = []
    for data in dict_['Similar']['Results']:
        lst.append(data['Name'])
    return lst


def get_related_titles(lst):
    """

    :param lst: list of movie titles
    :return: a combined list of similar movies for all titles in the input list
    """
    result_lst = []
    for movie in lst:
        json_movies = get_movies_from_tastedive(movie)
        for title in extract_movie_titles(json_movies):
            if title not in result_lst:
                result_lst.append(title)
    return result_lst


def get_movie_data(title):
    """

    :param title: movie title
    :return: dictionary with information about the movie title
    """
    params = {"t": title, "r": "json", "apikey": apikey}
    base_url = "http://www.omdbapi.com/"
    result = requests.get(base_url, params=params)
    print(result.url)
    return json.loads(result.text)


def get_movie_rating(dict_):
    """

    :param dict_: dictionary with information about the movie title
    :return: integer value of 'Rotten Tomatoes' rating
    """
    for rating in dict_['Ratings']:
        if rating['Source'] == 'Rotten Tomatoes':
            return int(rating['Value'][0:2])
    return 0


def get_sorted_recommendations(movies_list):
    """
    The movies should be sorted in descending order by their Rotten Tomatoes rating,
    as returned by the get_movie_rating function.
    Break ties in reverse alphabetic order, so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.

    :param movies_list: list of movie titles
    :return: a sorted list of related movie titles as output
    """
    related = get_related_titles(movies_list)
    print(related)
    tups = []
    for title in related:
        movie_data = get_movie_data(title)
        print(movie_data)
        tups.append((title, get_movie_rating(movie_data)))
    res_tup = sorted(tups, reverse=True, key=lambda x: (x[1], x[0]))
    return [name[0] for name in res_tup]


print(get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"]))


