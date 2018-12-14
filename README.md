# CS410 Project: Single-cell RNA search

## Setup Instructions

Create a python virtual environment with the following
packages:

```text
Django==2.1.4
numpy==1.15.4
pandas==0.23.4
```

You'll also need to download the SQLite database containing the corpus 
and the inverted index. It's big, but that's the cost of having some 
19k documents with a vocabulary size of ~32k.

```text
$ rsync -avzP external@dolores.uchicago.edu::cs410_external
Password: eye-snowman-america
```

This file should be downloaded and dropped alongside ``manage.py``

After the database is in place, activate your environment and run

```text
python manage.py
```
Then point your browser to 

```text
http://localhost:8000/engine/
```

## Introduction

## Implementation Details

The main components involved in this project are listed below
 
1. Creating an inverted index that contains both term frequency (TF) and inverse document frequency (IDF)
2. Implmenting the ranker using BM25 ranking methdology
3. Web application created using Python Django

#### Creating Inverted Index: 
The logic to create inverted index is present in file create_inverted_index.py present within scSearch directory. The *commit_chunk* method withi in the file creates updates the inverted index for the non-zero cell counts and updates the index. The index stores three components *term frequency, document id, and document frequency*

#### Implementing the ranker using BM25 methodology.
We have implemeted BM25 ranking methodology to rank the search results. BM25 is a robust ranking methodology that takes into account both term frequency and inverse document frequency. The implementation is present in the file rankers.py within scSearch/engine directory. 

In this file, *fast_ranking* method takes input query as an parameter and fetches the cells from the inverted index based on the inputs. The intermediate result is then passed onto *bm25_score* method that ranks the results based on BM25 formula. The sorted results are then passed on to the web application with an optional cut-off parameter 'k'

#### Web application using Python Django
We have created a web application to make it easier for the users to search the cells and view the results accrodingly. The web application is created using Pythin Django framework. The implementation of the web application is present under scSearch/engine directory.

## Usage
To use the application, please follow the set up instructions first. Once installed, navigate to the eb page mentioned and enter some cells in the search text box provided. Say for example add the terms "KRAS", "CDN4K" and "TP53" and click "Search". The cells that match to the corresponding genes will be displayed on the right. The results will be empty if the input genes doesn't match the any of the cells in the corpus.

## Team Members
* Dominic Fitzgerald (df6)
* Venslaus Prakash Arokiaraj (vpa2)
* Neha Pandey (npand4)
