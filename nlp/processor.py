"""
Text processor. Only support English.
  1. Takes an input string and convert it into an array of words.
  2. Convert the dictionary into a Python dict.
"""
import os
import csv
import requests

SPACY_API = 'https://spacy-api-dot-tylerlee-portfolio.appspot.com'
# SPACY_API = 'http://localhost:8080'


def import_dict(d=None):
    """
    :param d: Path to the dictionary file
    :return: Python dictionary with words and their annotations
    """
    if not d:
        cpath = os.path.dirname(os.path.realpath(__file__))
        d = os.path.join(cpath, "sentiment_dict_en.txt")
    with open(d, 'r') as rf:
        reader = csv.reader(rf, delimiter=",")
        # Header has no commas (manually checked)
        reader = [r for r in reader if len(r) == 2]
        ret = dict(zip([r[0] for r in reader], [r[1] for r in reader]))
    return ret


def lemmatize(sentence):
    """
    :param sentence: Input string
    :return: array of lemmatized words from the input
    """
    data = {
        'text': sentence,
        'model': 'en_core_web_sm'
    }
    r = requests.post(SPACY_API + '/lemma', data=data)
    return r.json()


def flatten(arr):
    return [j for i in arr for j in i]


def compute_score(words):
    word_dict = import_dict()
    scores = []
    for word in words:
        scores.append(int(word_dict.get(word, 0)))

    if len(scores) == 0:
        return 0
    else:
        return sum(scores) / len(scores)


if __name__ == '__main__':
    sentence = lemmatize('What a beautiful day!')    # ['my', 'name', 'be', 'tyler']
    print(sentence)
    print(compute_score(sentence))
