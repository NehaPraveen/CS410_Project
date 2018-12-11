from django.db import models

# Create your models here.


class Cell(models.Model):
    name = models.CharField(max_length=256)

    def get_gene_count(self, gene_name):
        self.genecount_set.filter(gene__name=gene_name)


class Gene(models.Model):
    name = models.CharField(max_length=64)


class GeneCount(models.Model):
    cell = models.ForeignKey('Cell', on_delete=models.CASCADE)
    gene = models.ForeignKey('Gene', on_delete=models.CASCADE)
    count = models.FloatField()
