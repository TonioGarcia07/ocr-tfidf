#!/usr/bin/env python

import sys

max_df = {}

for line in sys.stdin:
    line = line.strip()
    word_doc_id, tfidf = line.split("\t")
    word, doc_id = word_doc_id.replace("(", "").replace(")", "").split(",")
    tfidf = float(tfidf)

    if not max_df.get(doc_id):
        max_df[doc_id] = {word: tfidf}

    for w, t in max_df.get(doc_id).items():
        if tfidf > t:
            max_df[doc_id][word] = tfidf
            if len(max_df[doc_id].keys()) > 20:
                max_df[doc_id].pop(w)

for doc_id, maximums in max_df.items():
    for word, tfidf in maximums.items():
        print("%s\t%s\t%s" % (doc_id, word, str(tfidf)))
