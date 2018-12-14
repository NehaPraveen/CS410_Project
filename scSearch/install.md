# How to install scSearch

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
