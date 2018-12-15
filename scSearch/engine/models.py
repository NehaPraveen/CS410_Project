from django.db import models

# Create your models here.


class Cell(models.Model):
    name = models.CharField(max_length=256, unique=True)
    num_genes = models.IntegerField()
    num_transcripts = models.IntegerField()
    subtype = models.CharField(max_length=128)

    def get_top_k_genes(self, k=5):
        top_k = sorted(self.invertedindex_set.all(), key=lambda r: r.term_freq, reverse=True)[:5]
        return [(g.term_id.name, g.term_freq) for g in top_k]


class Gene(models.Model):
    name = models.CharField(max_length=64, unique=True)


class InvertedIndex(models.Model):
    term_id = models.ForeignKey('Gene', on_delete=models.CASCADE)
    doc_id = models.ForeignKey('Cell', on_delete=models.CASCADE)
    term_freq = models.IntegerField()

    class Meta:
        unique_together = ('term_id', 'doc_id')
