#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()

    word_file, count = line.split("\t")
    word, doc_id = word_file.split(",")

    print("%s\t%s,%s" % (doc_id, word, count))
