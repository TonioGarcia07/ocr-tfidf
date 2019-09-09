# 🕵️‍ TF-IDF

## Setup

Install [hadoop](https://www.google.com/search?q=hadoop).

Download the corpus:

- The Call of the Wild 🤠: `curl -X GET http://www.textfiles.com/etext/FICTION/callwild > callwild.txt`
- Robin Crusoé 🏐: `curl -X GET http://www.textfiles.com/etext/FICTION/defoe-robinson-103.txt > robin-crusoe.txt`

Place the files in HDFS (corpus and stopwords):

- `hadoop fs -put callwild.txt /input && hadoop fs -put defoe-robinson-103.txt /input` for the corpus.
- `hadoop fs -put stopwords_en.txt /` for the stop words (mapper1).

## 20 top results

Best results for Robinson Crusoé:

```
years       0.00139793119376
left        0.00181353235947
side        0.00226691544934
making      0.00139793119376
island      0.00345704606024
place       0.00377819241557
shore       0.00496832302647
large       0.0013601492696
days        0.00147349504207
country     0.00145460407999
kind        0.00143571311792
thoughts    0.00209689679064
day         0.00317368162908
water       0.00272029853921
friday      0.00338148221193
told        0.00226691544934
time        0.00523279649556
began       0.00343815509817
things      0.00313589970492
thought     0.00311700874284
```

Best results for The Call of the Wild:

```
perrault    0.00190552386364
traces      0.00144201805897
found       0.00133901676904
team        0.0015450193489
wolf        0.00133901676904
thing       0.00139051741401
face        0.00139051741401
camp        0.00272953418305
john        0.00206002579853
great       0.0025235316032
man         0.00473805933662
sled        0.00309003869779
trail       0.00211152644349
knew        0.00221452773342
fire        0.00164802063882
buck        0.0161197018735
dogs        0.00576807223588
spitz       0.00309003869779
thornton    0.00417155224202
work        0.00118451483415
```

## MapReduce functions

## Commands

- `hadoop jar hadoop-streaming.jar -input /input/robin-crusoe.txt -input /input/callwild.txt -output /output1 -mapper ./mapper1.py -reducer ./reducer1.py`
- `hadoop jar hadoop-streaming.jar -input /ouput1/part-00000 -output /output2 -mapper ./mapper2.py -reducer ./reducer2.py`
- `hadoop jar hadoop-streaming.jar -input /ouput2/part-00000 -output /output3 -mapper ./mapper3.py -reducer ./reducer3.py`
- `hadoop jar hadoop-streaming.jar -input /ouput3/part-00000 -output /results -mapper ./mapper4.py -reducer ./reducer4.py`

Précéder ces commandes de `hadoop fs -rm -r /output<i>` si vous voulez re-écrire l'output.
De même, lancez la commande `hadoop fs -cat /output<i>/part-00000` si vous voulez afficher la sortie de l'algorithme.

### 1st MapReduce

- `hadoop jar hadoop-streaming.jar -input /input/robin-crusoe.txt -input /input/callwild.txt -output /output1 -mapper ./mapper1.py -reducer ./reducer1.py`

**Input:** the words of the list.
**Output:** "word,doc_id count"

### 2nd MapReduce

- `hadoop jar hadoop-streaming.jar -input /ouput1/part-00000 -output /output2 -mapper ./mapper2.py -reducer ./reducer2.py`

**Input:** "word,doc_id count"
**Output:** "word,doc_id wordcount,wordperdoc"

### 3rd MapReduce

- `hadoop jar hadoop-streaming.jar -input /ouput2/part-00000 -output /output3 -mapper ./mapper3.py -reducer ./reducer3.py`

**Input:** "word,doc_id wordcount,wordperdoc"
**Output:** "word,doc_id tfidf"

### 4th Map only

- `hadoop jar hadoop-streaming.jar -input /ouput3/part-00000 -output /results -mapper ./mapper4.py -reducer ./reducer4.py`

**Input:** "word,doc_id tfidf"
**Output:** "doc_id word tfidf" (for the 20 max tf-idf)
