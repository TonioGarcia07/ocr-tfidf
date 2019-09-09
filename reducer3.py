#!/usr/bin/env python

from operator import itemgetter
import sys
import math

prev_word = None
prev_doc_id = None
prev_wordcount = None
prev_wordperdoc = None
n_doc = 1


def get_tfidf(word_count, word_per_doc, n_doc, N=2):
    return (word_count / float(word_per_doc)) * math.log(N / n_doc)


for line in sys.stdin:
    line = line.strip()
    word, rest = line.split("\t")
    doc_id, wordcount, wordperdoc = rest.split(",")

    wordcount = int(wordcount)
    wordperdoc = int(wordperdoc)

    if prev_word == word:
        # same word but for the other document -> print for the first
        n_doc = 2
        prev_tfidf = get_tfidf(prev_wordcount, prev_wordperdoc, n_doc)
        print("(%s,%s)\t%s" % (prev_word, prev_doc_id, prev_tfidf))
    else:
        # different word
        if prev_word is not None:
            prev_tfidf = get_tfidf(prev_wordcount, prev_wordperdoc, n_doc)
            print("(%s,%s)\t%s" % (prev_word, prev_doc_id, prev_tfidf))

    # reassign
    prev_word = word
    prev_doc_id = doc_id
    prev_wordcount = wordcount
    prev_wordperdoc = wordperdoc
    n_doc = 1

prev_tfidf = get_tfidf(prev_wordcount, prev_wordperdoc, n_doc)
print("(%s,%s)\t%s" % (prev_word, prev_doc_id, prev_tfidf))
