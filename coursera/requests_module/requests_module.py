import requests
import json

"""
Questions to ask when using REST API:
- What is the baseurl?
- What keys should you provide in the dictionary you pass for the params parameter?
- What values should you provide associated with those keys?
- Do you need to authenticate yourself as a licensed user of the API and, if so, how?
- What is the structure and meaning of the data that will be provided?
"""
def requests_practice():
    # retrieve data from specified URL
    page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
    assert page.status_code == 200, "The request failed"
    print("Sent GET request to URL: {}".format(page.url)) # print the url that was fetched
    print("Type of the returned data is: ", type(page))  # requests.Response
    print("You can use slice operation as with strings.\nFirst 150 symbols:\n{}".format(page.text[:150])) # print the first 150 characters

    print("-" * 150)
    print("Using page.json() you can turn page.text into a python object: ")
    page_json_obj = page.json() # turn page.text into a python object
    print("The type of the returned value is the same as result of json.loads(): {}".format(type(page_json_obj)))
    print("The first item in the list:\n{}".format(page_json_obj[0]))
    print("The first 10 elements of the list, pretty printed:\n{}".format(json.dumps(page_json_obj[:10], indent=2)))



""""
Task:
Print out the shortest abstract from the URL
http://api.plos.org/search?q=title:%22Drosophila%22%20and%20body:%22RNA%22&fl=id,abstract
"""
def shortest_text():
    page = requests.get("http://api.plos.org/search?q=title:%22Drosophila%22%20and%20body:%22RNA%22&fl=id,abstract")
    assert page.status_code == 200, "The request failed"
    page_python_obj = page.json()
    list_of_dicts = page_python_obj['response']['docs']
    id = ''
    abstract = list_of_dicts[0]['abstract'][0]
    shortest = len(abstract)
    for data in list_of_dicts:
        abstract_text = data['abstract'][0].strip()
        if len(abstract_text) < shortest:
            shortest = len(abstract_text)
            id = data['id']
            abstract = abstract_text
    print("The shortest abstract with id '{}' is:\n{}".format(id, abstract))

"""
The GET function in the requests module takes an optional parameter called params. 
If a value is specified for that parameter, it should be a dictionary. 
The keys and values in that dictionary are used to append something to the URL that is requested from the remote site.
"""
def request_with_params(word):
    kval_pairs = {'rel_rhy': word}
    page = requests.get("https://api.datamuse.com/words", params=kval_pairs)
    print(page.text[:150])  # print the first 150 characters
    print(page.url)  # print the url that was fetched
    print('en' in page.json()[0]['word'])

# requests_practice()
# shortest_text()
request_with_params('kitten')

