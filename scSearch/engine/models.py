from django.db import models

# Create your models here.


class Cell(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def get_gene_count(self, gene_name):
        self.genecount_set.filter(gene__name=gene_name)


class Gene(models.Model):
    name = models.CharField(max_length=64, unique=True)


class GeneCount(models.Model):
    cell = models.ForeignKey('Cell', on_delete=models.CASCADE)
    gene = models.ForeignKey('Gene', on_delete=models.CASCADE)
    count = models.FloatField()


class InvertedIndex(models.Model):
    term_id = models.ForeignKey('Gene', on_delete=models.CASCADE)
    doc_id = models.ForeignKey('Cell', on_delete=models.CASCADE)
    term_freq = models.IntegerField()

    class Meta:
        unique_together = ('term_id', 'doc_id')
