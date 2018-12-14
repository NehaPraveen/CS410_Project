from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from engine.rankers import fast_ranking

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
    for i, cell in enumerate(ranking, start=1):
        results.append({
            'name': cell,
            'subtype': 'Subtype Placeholder',
            'num_genes': '6',
            'num_transcripts': '8',
            'top_five_genes': [
                ['KRAS', '5'],
                ['TP53', '3'],
                ['SMAD4', '18'],
                ['CDNK4D', '9'],
                ['MMN', '2']
            ]
        })

    return render(request, 'engine/search_result.html', context={'results': results})
