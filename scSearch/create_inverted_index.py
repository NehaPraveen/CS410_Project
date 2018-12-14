import os
import math
import django
from django.db.transaction import atomic
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scSearch.settings')
django.setup()

from engine.models import InvertedIndex, Cell, Gene

chunk_size = 100
df_reader = pd.read_csv('../GTEx_droncseq_hip_pcf/GTEx_scRNAseq_genes_TPM.final.csv', chunksize=chunk_size)
n_rows = 32090
n_chunks = math.ceil(n_rows / chunk_size)


@atomic
def commit_chunk(chunk_df):
    for i, row in chunk_df.iterrows():
        gene = row['gene_name']
        nonzero = row[row != 0].drop('gene_name')
        for cell, term_freq in nonzero.iteritems():
            ii_entry = InvertedIndex(
                term_id=Gene.objects.get(name=gene),
                doc_id=Cell.objects.get(name=cell),
                term_freq=term_freq
            )
            ii_entry.save()


for chunk_i, chunk_df in enumerate(df_reader):
    print('Reading in chunk {}/{}'.format(chunk_i + 1, n_chunks))
    commit_chunk(chunk_df)

