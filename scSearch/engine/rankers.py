from collections import Counter
import numpy as np

from engine.models import InvertedIndex, Cell


def document_frequency(w):
    return InvertedIndex.objects.filter(term_id__name=w).count()


def bm25_score(q, d_counts, k=300, n_docs=14963):
    words = set(q).intersection(set(d_counts.keys()))
    q_counts = Counter(q)

    score = 0
    for word in words:
        t1 = q_counts[word]
        t2 = ((k+1) * d_counts[word]) / (d_counts[word] + k)
        t3 = np.log((n_docs+1) / (document_frequency(word)))
        score += t1 * t2 * t3

    return score


def fast_ranking(query, top_k=None):
    n_docs = Cell.objects.all().count()

    # candidate_docs_index = InvertedIndex.objects.filter(term_id__name__in=set(query))
    candidate_docs_index = {idx.doc_id.name for idx in InvertedIndex.objects.filter(term_id__name__in=set(query))}

    doc_scores = dict()
    for doc in candidate_docs_index:
        d_counts = {
            q: getattr(InvertedIndex.objects.filter(term_id__name=q, doc_id__name=doc).first(), 'term_freq', 0)
            for q in set(query)
        }
        doc_scores[doc] = bm25_score(query, d_counts, n_docs=n_docs)

    # Sort into a ranked list, optionally returning top k results
    return sorted(doc_scores.items(), key=lambda r: r[1], reverse=True)[:top_k]
