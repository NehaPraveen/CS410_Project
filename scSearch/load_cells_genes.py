import os
import django
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scSearch.settings')
django.setup()

from engine.models import Cell, Gene

CORPUS_CSV = '../GTEx_droncseq_hip_pcf/GTEx_scRNAseq_genes_TPM.final.csv'

print('Loading cell names')
cells = pd.read_csv(CORPUS_CSV, nrows=1).drop(columns='gene_name').columns.values
for cell in cells:
    Cell.objects.get_or_create(name=cell)

print('Loading gene names')
genes = pd.read_csv(CORPUS_CSV, usecols=['gene_name'])['gene_name'].values
for gene in genes:
    Gene.objects.get_or_create(name=gene)
