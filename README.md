# CS410 Project: Single-cell RNA search

## Setup Instructions

Create a Python virtual environment with the following
packages:

```text
Django==2.1.4
numpy==1.15.4
pandas==0.23.4
```

You'll also need to download the SQLite database containing the corpus 
and the inverted index. It's big, but that's the cost of having some 
19k documents with a vocabulary size of ~32k:

```text
$ rsync -avzP external@dolores.uchicago.edu::cs410_external
Password: eye-snowman-america
```

This file should be downloaded and dropped alongside ``scSearch/manage.py``

After the database is in place, activate your environment and run

```text
python manage.py runserver
```
Then point your browser to 

```text
http://localhost:8000/engine/
```

Alternatively, there is a live version available at 

```text
http://djf604.com:8000/engine/
```

## Introduction

Single-cell RNA sequencing (scRNAseq) is a relatively novel biotechnology which isolates individual cells before 
sequencing. This allows researchers to take a snapshot of RNA activity in a given cell, as opposed to a chunk of tissue 
as in bulk RNAseq.

Gene expression in a single cell, however, can be very sparse, with most genes not having enough expression to 
differentiate from zero. While this presents certain challenges, it also likens 
the problem to those faced by Text Retrieval and Text Mining techniques. Individual cells can be considered "documents" 
which contain a "bag of genes/words". Because there is a finite number of genes that can be expressed by a cell in a 
given organism, the vocabulary of "words" is finite as well.

Given the above context, we decided to create a search engine for scRNAseq cells, called *scSearch*. Users input a list 
of gene names along with weights and are returned a ranked list of the top 10 cells which most closely match the query. 
Some metadata about the genes is given to aid researchers in biological interpretation. The corpus is built from 
publicly available scRNAseq expression data from the [GTEx](https://gtexportal.org/home/) project.

## Implementation Details

The main components involved in this project are listed below
 
1. Creating an inverted index that contains both term frequency (TF) and inverted document frequency (IDF)
2. Implementing the ranker using BM25 ranking methodology
3. Web application created using Python Django

#### Creating Inverted Index
The logic to create the inverted index is present in the file ``create_inverted_index.py`` present within the ``scSearch/`` 
directory. The TPM-normalized (see below) dataset is passed as input and the data is read in chunks with chunk size 
set to 100 lines.  The ``commit_chunk()`` method commits a batch of inverted index entries to the database for 
non-zero gene counts. The index stores three components ``<gene id, cell id, gene frequency>``.

#### Implementing the ranker using BM25 methodology
We have implemented the BM25 ranking methodology to rank the search results. BM25 is a robust ranking methodology that 
takes into account both term frequency and inverse document frequency. The implementation is present in the file 
``rankers.py`` within the ``scSearch/engine/`` directory. 

In this file, the ``fast_ranking()`` method takes a query vector as a parameter and fetches the cells from the 
inverted index based on the inputs. The intermediate result is then passed onto the ``bm25_score()`` method that 
ranks the results based on BM25 formula. The sorted results are then passed on to the web application with an 
optional cut-off parameter ``k``.

#### A note about document length normalization

Document length normalization is one place where the scRNAseq to Text Retrieval problem doesn't quite translate. Raw gene 
counts must be normalized because of differences in gene length: longer genes are more likely to have reads align to them 
by chance, so their counts may be artificially inflated. The normalization metric implicity used here, TPM, takes these 
factors into account when determining gene expression. Therefore, our raw data (in TPM units) are already document 
length normalized, so that term was left out of our BM25 scoring function.

#### Web application using Python Django
We have created a web application to make it easier for users to search the cells and view the results accordingly. 
The web application was created using the Python Django framework. The implementation of the web application is 
present under ``scSearch/engine/`` directory.

## Usage
To use the application, please follow the set up instructions first. Once installed, navigate to the web page mentioned 
and enter some genes in the left panel search box. Say for example add the genes "KRAS", "CDN4K", and "TP53" and 
click "Search". The cells that match the corresponding genes will be displayed on the right. The results will be 
empty if the input genes don't match the any of the cells in the corpus.

## Team Members
* Dominic Fitzgerald (df6)
* Venslaus Prakash Arokiaraj (vpa2)
* Neha Pandey (npand4)
