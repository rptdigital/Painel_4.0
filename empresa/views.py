
from django.shortcuts import render
from .models import Empresa, Proposta, Comb_Servico, Servico, Responsavel, Contato,Area, Nivel_hierarquico, Modulo, Estagio, Projeto, StatusProjeto, Linha_de_servico
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Value, CharField, Prefetch, Sum, F
from django.db.models.functions import Concat
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

#def homepage(request):
#    return render(request, "homepage.html")

class Homepage(TemplateView):
    template_name = "homepage.html"


#def homeempresa(request):
#
#   context = {}
#   lista_empresas = Empresa.objects.all()
#    context['lista_empresas'] = lista_empresas
#    return render(request, "homeempresa.html", context)

class Homeempresas(ListView):
    template_name = "homeempresas.html"
    model = Empresa


class Perfilempresa(DetailView):
    template_name = "perfilempresa.html"
    model = Empresa

    def get_context_data(self, **kwargs):
        context = super(Perfilempresa, self).get_context_data(**kwargs)
        empresa_id = self.object.id  # Obtemos o ID da empresa atual

        # Filtra propostas associadas à empresa
        modulos_prefetch = Prefetch('modulos', queryset=Comb_Servico.objects.select_related('modulo__servico'))
        propostas = Proposta.objects.filter(empresa_id=empresa_id).select_related('estagio').prefetch_related(modulos_prefetch)
        context['propostas'] = propostas

        # Filtra responsáveis associados às propostas da empresa
        responsaveis_ids = propostas.values_list('responsavel', flat=True).distinct()
        context['responsaveis'] = Responsavel.objects.filter(id__in=responsaveis_ids)

        # Obter empresas associadas aos contatos
        context['empresas_unicas'] = Empresa.objects.filter(contatos__isnull=False).values_list('id', 'nome').distinct().order_by('nome')

        # Adicionar cálculo para projetos fechados e total gasto
        propostas_fechadas = propostas.filter(estagio__nome='Aprovado')
        total_projetos_fechados = propostas_fechadas.count()
        total_gasto = propostas_fechadas.aggregate(Sum('valor'))['valor__sum'] or 0

        context['total_projetos_fechados'] = total_projetos_fechados
        context['total_gasto'] = total_gasto

        # Adicionar código para encontrar o último projeto aprovado
        ultimo_projeto_fechado = propostas_fechadas.order_by('-data_de_aprovacao').first()
        context['ultimo_projeto_fechado'] = ultimo_projeto_fechado

        # Buscar propostas e preparar dados para o gráfico
        propostas_grafico = propostas.annotate(
            nome_do_projeto=F('nome'),
            estagio_do_projeto=F('estagio__nome'),  # Modificado aqui para usar o nome do estágio
            responsavel_do_projeto=F('responsavel__nome'),
            data_de_aprovacao_do_projeto=F('data_de_aprovacao')
        ).values(
            'nome_do_projeto', 'estagio_do_projeto', 'responsavel_do_projeto', 
            'data_de_pedido', 'data_de_aprovacao_do_projeto'
        )

        # Formatar os dados para o gráfico
        propostas_grafico_formatted = [
            {
                'data_de_pedido': proposta['data_de_pedido'].strftime("%Y-%m-%d") if proposta['data_de_pedido'] else None,
                'nome': proposta['nome_do_projeto'],
                'estagio': proposta['estagio_do_projeto'],
                'responsavel': proposta['responsavel_do_projeto'],
                'data_de_aprovacao': proposta['data_de_aprovacao_do_projeto'].strftime("%Y-%m-%d") if proposta['data_de_aprovacao_do_projeto'] else None
            } for proposta in propostas_grafico
        ]
        
        context['propostas_grafico'] = json.dumps(propostas_grafico_formatted, cls=DjangoJSONEncoder)

        return context



class PropostasListView(ListView):
    model = Proposta
    template_name = 'propostas.html'  # Caminho para o seu template

    def get_queryset(self):
        # Prefetch os módulos e, por sua vez, os serviços
        modulos_prefetch = Prefetch('modulos__modulo', queryset=Modulo.objects.select_related('servico'))
        return Proposta.objects.prefetch_related(modulos_prefetch).all()

    def get_context_data(self, **kwargs):
        context = super(PropostasListView, self).get_context_data(**kwargs)
        
        servico_ids = Comb_Servico.objects.values_list('modulo__servico_id', flat=True).distinct()

       # Obter empresas associadas a propostas
        context['empresas_unicas'] = Empresa.objects.filter(propostas__isnull=False).values_list('id', 'nome').distinct().order_by('nome')

        # Obter serviços associados a propostas
        context['servicos_unicos'] = Servico.objects.filter(id__in=servico_ids).values_list('id', 'nome').distinct().order_by('nome')

        # Obter responsáveis associados a propostas
        context['responsaveis_unicos'] = Responsavel.objects.filter(propostas__isnull=False).values_list('id', 'nome').distinct().order_by('nome')

        # Adicionar estágios ao contexto
        context['estagios'] =  Estagio.objects.all()

        return context



#Ajustar e tirar as funções só para teste --->
class ContatosListView(ListView):
    model = Contato
    template_name = 'contatos.html'

    def get_queryset(self):
        return Contato.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ContatosListView, self).get_context_data(**kwargs)

        # Obter nomes únicos de áreas
        context['areas_unicas'] = Area.objects.values_list('nome', flat=True).distinct().order_by('nome')

        # Obter nomes únicos de níveis hierárquicos
        context['niveis_unicos'] = Nivel_hierarquico.objects.values_list('nome', flat=True).distinct().order_by('nome')

        # Combina 'nome' e 'sobrenome' para cada contato
        context['nomes_contatos'] = Contato.objects.annotate(
            nome_completo=Concat('nome', Value(' '), 'sobrenome', output_field=CharField())
        ).values_list('nome_completo', flat=True).distinct().order_by('nome_completo')

        # Obter empresas associadas aos contatos
        context['empresas_unicas'] = Empresa.objects.filter(contatos__isnull=False).values_list('id', 'nome').distinct().order_by('nome')

        for contato in context['object_list']:
            print(contato.nome, contato.CC)  # Isso deve imprimir os nomes e os valores de CC no console
        
        return context


class DragAndDropView(TemplateView):
    template_name = "kanban.html"

    def filtrar_propostas_por_estagio(self, estagio_nome):
        propostas = Proposta.objects.filter(estagio__nome=estagio_nome).select_related('empresa')
        return [{'id': proposta.id, 'descricao': f"{proposta.empresa.nome} - {proposta.nome}"} for proposta in propostas]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empresas'] = Empresa.objects.all()

        # Filtrar propostas por estágio e adicionar ao contexto
        context['qualificado_propostas'] = self.filtrar_propostas_por_estagio('Qualificado')
        context['desenvolvimento_propostas'] = self.filtrar_propostas_por_estagio('Desenvolvimento')
        context['apresentacao_propostas'] = self.filtrar_propostas_por_estagio('Apresentação')
        context['enviada_propostas'] = self.filtrar_propostas_por_estagio('Enviada')
        context['aprovado_propostas'] = self.filtrar_propostas_por_estagio('Aprovado')
        context['declinada_propostas'] = self.filtrar_propostas_por_estagio('Declinada')

        return context

    

class DragAndDropView_Projetos(TemplateView):
    template_name = "projeto_kanban.html"   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        linha_servico_id = self.request.GET.get('linha_servico')

        def filtrar_projetos_por_status_e_linha_servico(status_nome):
            query = Projeto.objects.filter(status_projeto__nome=status_nome)
            if linha_servico_id:
                query = query.filter(proposta__modulos__modulo__servico__linha_de_servico_id=linha_servico_id).distinct()
            return query

        context['nao_iniciado_projetos'] = filtrar_projetos_por_status_e_linha_servico('Não iniciado')
        context['em_andamento_projetos'] = filtrar_projetos_por_status_e_linha_servico('Em andamento')
        context['pausado_e_cancelados_projetos'] = filtrar_projetos_por_status_e_linha_servico('Pausado/Cancelado')
        context['fechamento_em_vista_projetos'] = filtrar_projetos_por_status_e_linha_servico('Fechamento em vista')
        context['concluidos_vista_projetos'] = filtrar_projetos_por_status_e_linha_servico('Concluído')

        # Certifique-se de que não há duplicatas nas linhas de serviço
        context['linhas_de_servico'] = Linha_de_servico.objects.order_by('nome')


        return context



@csrf_exempt
def update_status(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        projeto_id = data['projectId']
        novo_status_nome = data['newStatus']

        try:
            projeto = Projeto.objects.get(pk=projeto_id)
            novo_status = StatusProjeto.objects.get(nome=novo_status_nome)
            projeto.status_projeto = novo_status
            projeto.save()
            return JsonResponse({"success": True})
        except (Projeto.DoesNotExist, StatusProjeto.DoesNotExist):
            return JsonResponse({"success": False, "error": "Projeto ou Status não encontrado"}, status=404)

    return JsonResponse({"success": False}, status=400)

@csrf_exempt
def create_proposta(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            empresa_id = data.get('empresa_id')
            estagio_nome = data.get('estagio_nome', 'Qualificado')  # Definir um nome padrão

            empresa = Empresa.objects.get(id=empresa_id)
            estagio, created = Estagio.objects.get_or_create(nome=estagio_nome)  # Obter ou criar o estágio

            proposta = Proposta(
                empresa=empresa,
                nome='Nome da Nova Proposta',
                estagio=estagio,
                valor=0,  # Valor padrão
                # Outros campos conforme necessário...
            )
            proposta.save()

            return JsonResponse({'success': True, 'proposta_id': proposta.id})
        except Empresa.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Empresa não encontrada.'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    else:
        return JsonResponse({'success': False, 'error': 'Método HTTP inválido.'}, status=405)


@csrf_exempt
def update_proposta_estagio(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            proposta_id = data.get('proposta_id')
            estagio_nome = data.get('estagio_nome')

            proposta = Proposta.objects.get(id=proposta_id)
            estagio = Estagio.objects.get(nome=estagio_nome)
            proposta.estagio = estagio
            proposta.save()

            proposta_id = int(data.get('proposta_id'))

            return JsonResponse({'success': True})
        except Proposta.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Proposta não encontrada.'}, status=400)
        except Estagio.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Estágio não encontrado.'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    else:
        return JsonResponse({'success': False, 'error': 'Método HTTP inválido.'}, status=405)
