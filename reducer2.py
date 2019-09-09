#! /usr/bin/env python3

import sys


prev_doc_id = None
N = 0
df = {}
lines = []

for line in sys.stdin:
    line = line.strip()
    lines.append(line)

    doc_id, word_count = line.split("\t")
    word, count = word_count.split(",")
    count = int(count)

    if prev_doc_id == doc_id:
        N = N + count
    else:
        if prev_doc_id is not None:
            df[prev_doc_id] = N
        N = count
        prev_doc_id = doc_id

df[prev_doc_id] = N


for h in lines:
    doc_id, word_count = h.split("\t")
    word, count = word_count.split(",")

    print("%s,%s\t%s,%d" % (word, doc_id, count, df[doc_id]))
