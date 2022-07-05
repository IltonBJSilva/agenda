from django.db import models
from django.contrib.auth.models import User
# Create your models here.


#Criar as tabelas

class Evento(models.Model):
    #Criação dos campos do banco de dados
    titulo = models.CharField(max_length=100,verbose_name='Titulo')
    descricao = models.TextField(blank=True, null=True,verbose_name='descricao')
    #Criação para campos onde vai conter datas
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    #O parametro que vai receber seria de sempre que for criado um novo registro
    #Vai inserir a hora atual nesse campo quando inseri
    data_criacao = models.DateTimeField(auto_now=True,verbose_name='Data da criação')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #Usando a tabela de usuarios do Django e se for excluido da aplicação, exclui todos eventos dele

    #criar uma tabela apenas com o nome dos eventos
    class Meta:
        db_table = 'evento' #Exigindo que a tabela se chame evento

    def __str__(self):
        return self.titulo #sempre que chamar esse objeto, vai trazer o nome do titulo



