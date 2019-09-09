#!/usr/bin/env python

import sys
import os
import re

doc_id = 0
switch = 1

for line in sys.stdin:
    line = line.strip()

    if switch == 1:
        if line == "1903":
            doc_id = 2
            switch = 0
        else:
            doc_id = 1
            switch = 0

    stopwords = []
    for sline in open("stopwords_en.txt"):
        stopwords.append(sline.strip())

    words = line.split()
    words = [word.lower() for word in words]
    words = [re.sub(r"[^\w]", "", word) for word in words]
    words = [word for word in words if word not in stopwords]
    words = [word for word in words if len(word) > 2]

    for word in words:
        print("%s,%d\t%d" % (word, doc_id, 1))
