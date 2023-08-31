from django.db import models

# Create your models here.

class Corredor(models.Model):
    numero = models.IntegerField()

    def __str__(self):
        return f'{self.numero}'

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='imagens/')
    corredor = models.ForeignKey(Corredor, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome