from django.shortcuts import render

from engine.rankers import fast_ranking
from engine.models import Cell

import json

# Create your views here.
def index(request):
    return render(request, 'engine/base.html')


def gene_card_ajax(request, gene, weight):
    context = {
        'gene': gene,
        'weight': weight
    }
    return render(request, 'engine/gene_cards.html', context)


def search_results_ajax(request, json_query_str):
    query_obj = json.loads(json_query_str)
    query = list()
    for gene, weight in query_obj.items():
        query += [gene] * weight
    ranking = [r[0] for r in fast_ranking(query, top_k=10)]

    results = list()
    for i, cell_name in enumerate(ranking, start=1):
        cell = Cell.objects.get(name=cell_name)
        results.append({
            'name': cell_name,
            'subtype': cell.subtype,
            'num_genes': cell.num_genes,
            'num_transcripts': cell.num_transcripts,
            'top_five_genes': cell.get_top_k_genes(k=5)
        })

    return render(request, 'engine/search_result.html', context={'results': results})
