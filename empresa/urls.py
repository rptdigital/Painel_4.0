
from django.urls import path, include
from .views import Homepage, Homeempresas, Perfilempresa, PropostasListView, ContatosListView,DragAndDropView,DragAndDropView_Projetos
from . import views

app_name = 'empresa'

urlpatterns = [
    path('', Homepage.as_view(), name="homepage"),
    path('empresas/' , Homeempresas.as_view(), name="homeempresas"),
    path('empresas/<int:pk>', Perfilempresa.as_view(), name="perfilempresa"),
    path('propostas/', PropostasListView.as_view(), name='propostas'),
    path('contatos/', ContatosListView.as_view(), name='contatos'),
    path('kanban/', DragAndDropView.as_view(), name='kanban'),
    path('projeto_kanban/', DragAndDropView_Projetos.as_view(), name='projeto_kanban'),
    path('update_project_status/', views.update_status, name='update_status'),
    path('create_proposta/', views.create_proposta, name='create_proposta'),
    path('update_proposta_estagio/', views.update_proposta_estagio, name='update_proposta_estagio'),
]

