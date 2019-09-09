#!/usr/bin/env python

import sys
import os


for line in sys.stdin:
    line = line.strip()
    word_doc_id, counts = line.split("\t")
    word, doc_id = word_doc_id.split(",")
    wordcount, wordperdoc = counts.split(",")

    print("%s\t%s,%s,%s" % (word, doc_id, wordcount, wordperdoc))
