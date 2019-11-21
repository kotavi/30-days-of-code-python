import requests

"""
ml - means like constraint;
sl - sounds like constraint;
sp - spelled like constraint;
rel_[code]	Related word constraints: require that the results, when paired with the word in this parameter, are in a predefined lexical relation indicated by [code]. Any number of these parameters may be specified any number of times. An assortment of semantic, phonetic, and corpus-statistics-based relations are available. At this time, these relations are available for English-language vocabularies only.

words that rhyme with forgetful	/words?rel_rhy=forgetful
words that rhyme with grape that are related to breakfast	/words?ml=breakfast&rel_rhy=grape
adjectives that are often used to describe ocean	/words?rel_jjb=ocean
adjectives describing ocean sorted by how related they are to temperature	/words?rel_jjb=ocean&topics=temperature
nouns that are often described by the adjective yellow	/words?rel_jja=yellow
words that often follow "drink" in a sentence, that start with the letter w	/words?lc=drink&sp=w*
words that are triggered by (strongly associated with) the word "cow"	/words?rel_trg=cow
suggestions for the user if they have typed in rawand so far	/sug?s=rawand
"""
class DatamuseApi:

    def __init__(self, url="https://api.datamuse.com"):
        self.url = url

    def get_words_with_similar_meaning(self, phrase="ringing in the ears"):
        data = {"ml": phrase}
        return requests.get(self.url + "/words", params=data)

    def get_words_related_to(self, word="duck", sp="b*"):
        data = {"ml": word, "sp": sp}
        return requests.get(self.url + "/words", params=data)

    def get_words_sounds_like(self, word="elefint"):
        data = {"sl": word}
        return requests.get(self.url + "/words", params=data)

    def get_words_by_regex(self, regex="t??k"):
        data = {"sp": regex}
        return requests.get(self.url + "/words", params=data)

    def get_words_spelled_similarly(self, word="coneticut"):
        data = {"sp": word}
        return requests.get(self.url + "/words", params=data)