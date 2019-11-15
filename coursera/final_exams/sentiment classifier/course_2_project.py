
"""
We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file
named project_twitter_data.csv which has the text of a tweet, the number of retweets of that tweet,
and the number of replies to that tweet. We have also words that express positive sentiment and negative sentiment,
in the files positive_words.txt and negative_words.txt.
Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is.
You will create a csv file, which contains columns for the Number of Retweets, Number of Replies,
Positive Score (which is how many happy words are in the tweet), Negative Score
(which is how many angry words are in the tweet), and the Net Score for each tweet.
At the end, you upload the csv file to Excel or Google Sheets, and produce a graph
of the Net Score vs Number of Retweets.
To start, define a function called strip_punctuation which takes one parameter,
a string which represents a word, and removes characters considered punctuation
from everywhere in the word. (Hint: remember the .replace() method for strings.)

"""
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def strip_punctuation(a_word):
    for s in a_word:
        if s in punctuation_chars:
            a_word = a_word.replace(s, '')
    return a_word


def get_pos(sentences):
    count = 0
    for word in sentences.split():
        clean_word = strip_punctuation(word)
        if clean_word in positive_words:
            count += 1
    return count


def get_neg(sentences):
    count = 0
    for word in sentences.split():
        clean_word = strip_punctuation(word)
        if clean_word in negative_words:
            count += 1
    return count


project_twitter_data_file = open('project_twitter_data.csv', 'r')
project_twitter_data = project_twitter_data_file.readlines()

result_file = open('resulting_data.csv', 'w')


def write_header_to_csv():
    # tweet_text, retweet_count, reply_count = project_twitter_data[0].strip().split(',')
    header = "{}, {}, {}, {}, {}".format("Number of Retweets", "Number of Replies", "Positive Score", "Negative Score",
                                         "Net Score")
    result_file.write(header)
    result_file.write('\n')


write_header_to_csv()
for line in project_twitter_data[1:]:
    tweet_text, retweet_count, reply_count = line.strip().split(',')
    pos_number = get_pos(tweet_text)
    neg_number = get_neg(tweet_text)
    csv_line = "{},{},{},{},{}".format(retweet_count, reply_count, pos_number, neg_number, pos_number - neg_number)
    result_file.write(csv_line)
    result_file.write('\n')


