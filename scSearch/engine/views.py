from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return render(request, 'engine/base.html')


def gene_card_ajax(request, gene, weight):
    context = {
        'gene': gene,
        'weight': weight
    }
    return render(request, 'engine/gene_cards.html', context)
