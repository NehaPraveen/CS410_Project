import os
import django
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scSearch.settings')
django.setup()

from engine.models import Cell

METADATA_CSV = '../GTEx_droncseq_hip_pcf/nmeth.4407-S10.csv'
metadata = pd.read_csv(METADATA_CSV)

for i, row in metadata.iterrows():
    cell = Cell.objects.get(name=row['Cell ID'])
    cell.num_genes = row['#Genes ']
    cell.num_transcripts = row['#Transcripts']
    cell.subtype = row['Cluster Name']
    cell.save()
