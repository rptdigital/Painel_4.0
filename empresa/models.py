
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
#Listas Suspensas utilizadas nos bancos


# Banco empresas
class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    setor = models.ForeignKey("Setor", related_name='empresas', on_delete=models.CASCADE, null=True)
    logo = models.ImageField(upload_to='logo_empresas')
    descricao = models.TextField(max_length=2000)
    cidade = models.ForeignKey("Cidade", related_name='empresas', on_delete=models.CASCADE, null=True)
    data_de_criacao = models.DateTimeField(default=timezone.now)
    data_de_modificacao = models.DateTimeField(default=timezone.now())
    responsavel = models.ForeignKey("Responsavel",  related_name='empresas', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome


# Banco propostas
class Proposta(models.Model):
    empresa = models.ForeignKey("Empresa", related_name='propostas', on_delete=models.PROTECT)
    nome = models.CharField(max_length=150)
    deadline = models.DateTimeField(default=timezone.now())
    data_de_envio = models.DateTimeField(default=timezone.now())
    data_de_pedido = models.DateTimeField(default=timezone.now)
    data_de_aprovacao = models.DateTimeField(default=timezone.now())
    responsavel = models.ForeignKey("Responsavel", related_name='propostas', on_delete=models.CASCADE, null=True)
    estagio = models.ForeignKey("Estagio",  related_name='propostas', on_delete=models.CASCADE, null=True)
    valor = models.FloatField()

    def __str__(self):
        return self.empresa.nome + " - " + self.nome


# Banco Combinação Serviços
class Comb_Servico(models.Model):
    proposta = models.ForeignKey("Proposta", related_name='modulos', on_delete=models.CASCADE, null=True)
    modulo = models.ForeignKey("Modulo", related_name='combinacoes_servicos', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.proposta.nome 


#Banco módulo
class Modulo(models.Model):
    nome = models.CharField(max_length=150)
    servico = models.ForeignKey("Servico", related_name='modulo', on_delete=models.CASCADE , null=True)

    def __str__(self):
        return self.servico.nome + " - " + self.nome
    

# Banco Serviço
class Servico(models.Model):
    nome = models.CharField(max_length=150)
    linha_de_servico = models.ForeignKey("Linha_de_servico", related_name='servicos', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome


# Banco Linha de Serviço
class Linha_de_servico(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome


# Banco Contato
class Contato(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    nivel_hierarquico = models.ForeignKey("Nivel_hierarquico", related_name='contato', on_delete=models.CASCADE)
    area = models.ForeignKey("Area", related_name='contato', on_delete=models.CASCADE)
    CC = models.BooleanField()
    telefone = models.CharField(max_length=11, null= True, 
        validators=[
            RegexValidator(
                regex='^\\d{8}$',
                message='O número do telefone deve conter exatamente 8 dígitos.',
                code='invalid_tell_number'
            )
        ])
    celular = models.CharField(max_length=11, null= True,
        validators=[
            RegexValidator(
                regex='^\\d{11}$',
                message='O número de celular deve conter exatamente 11 dígitos.',
                code='invalid_cell_number'
            )
        ])
    email = models.EmailField()
    endereco = models.ForeignKey("Endereco", related_name='contato', on_delete=models.CASCADE, null=True)
    empresa = models.ForeignKey("Empresa", related_name="contatos", on_delete = models.PROTECT)  
    

    def __str__(self):
        return self.nome + " " + self.sobrenome
    

#Banco Nível hierarquico
class Nivel_hierarquico(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

#Banco Área que o contato trabalha
class Area(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome


#Banco cidade
class Cidade(models.Model):
    nome = models.CharField(max_length=150)
    estado = models.ForeignKey("Estado", related_name='cidade', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


#Banco Estado
class Estado(models.Model):
    nome = models.CharField(max_length=150)
    uf = models.CharField(max_length=3)
    pais = models.ForeignKey("Pais", related_name='estado', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


#Banco Pais
class Pais(models.Model):
    nome = models.CharField(max_length=200)
   
    def __str__(self):
        return self.nome


#Banco de Responsáveis 
class Responsavel(models.Model):
    nome = models.CharField(max_length=200)
   
    def __str__(self):
        return self.nome  
    

#Banco de Setor
class Setor(models.Model):
    nome = models.CharField(max_length=200)
   
    def __str__(self):
        return self.nome  


#Banco de Endereço 
class Endereco(models.Model):
    nome = models.CharField(max_length=200)
    numero = models.CharField(max_length=200)
    cep = models.CharField(max_length=8,
        validators=[
            RegexValidator(
                regex='^\\d{8}$',
                message='O cep deve conter exatamente 8 dígitos.',
                code='invalid_cell_number'
            )
        ])
    bairro = models.CharField(max_length=200)
    complemento = models.CharField(max_length=200, null=True)
    cidade = models.ForeignKey("Cidade", related_name='endereco', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome  
    

#Banco de Setor
class Estagio(models.Model):
    nome = models.CharField(max_length=200)
   
    def __str__(self):
        return self.nome  

#Banco de projetos
class Projeto(models.Model):
    proposta = models.OneToOneField('Proposta', on_delete=models.CASCADE, related_name='projeto')
    data_de_cadastro = models.DateTimeField(auto_now_add=True)
    status_projeto = models.ForeignKey('StatusProjeto', related_name='projetos', on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.status_projeto is None:  # Se nenhum status for fornecido, definir para 'Não iniciado'
            status_nao_iniciado, _ = StatusProjeto.objects.get_or_create(nome='Não iniciado')
            self.status_projeto = status_nao_iniciado
        super(Projeto, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.proposta.empresa.nome} - {self.proposta.nome}"
    
@receiver(post_save, sender=Proposta)
def criar_projeto_para_proposta_aprovada(sender, instance, **kwargs):
    if instance.estagio.nome == 'Aprovado' and not hasattr(instance, 'projeto'):
        status_nao_iniciado, _ = StatusProjeto.objects.get_or_create(nome='Não iniciado')
        Projeto.objects.create(proposta=instance, status_projeto=status_nao_iniciado)



#Banco de status dos projetos
class StatusProjeto(models.Model):
    nome = models.CharField(max_length=200, default='Não iniciado')
   
    def __str__(self):
        return self.nome  
