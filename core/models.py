from django.db import models

class Uva(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to='imagens/')

    def __str__(self):
        return self.nome
class Cor(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    categoria = models.CharField(max_length=50)
    created_at = models.DateField()
    updated_at = models.DateField()
    imagem = models.ImageField(upload_to='media/imagens/')

    
    def __str__(self):
        return self.nome

class Vinho(models.Model):
    nome = models.CharField(max_length=100)
    teorAlc = models.CharField(max_length=50)
    tempAmbServ = models.CharField(max_length=50)
    data = models.DateField()
    local = models.CharField(max_length=50)
    safra = models.CharField(max_length=50)
    produtor = models.CharField(max_length=100)
    paisRegiao = models.CharField(max_length=100)
    degustador = models.CharField(max_length=1000)
    rotulo = models.CharField(max_length=255)
    uva_id = models.ForeignKey('Uva', models.DO_NOTHING)
    
    def __str__(self):
        return self.nome        