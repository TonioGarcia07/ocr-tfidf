#!/usr/bin/env python

import sys

# Input:
# yelling,1       2
# yellings,1      1
# yellow,1        1
# yellow,2        5

# Map Output:
# 1         yelling,2
# 1         yellings,1
# 1         yellow,1
# 2         yellow,5

# Shuffle-sort output:
# (1, [(yelling,2), (yellings,1), (yellow,1)]
# (2, [(yellow,5)]

# Reduce output:
# (1, [(yelling,2), (yellings,1), (yellow,1)]
# (2, [(yellow,5)]

for line in sys.stdin:
    line = line.strip()

    word_file, count = line.split("\t")
    word, doc_id = word_file.split(",")

    print("%s\t%s,%s" % (doc_id, word, count))
