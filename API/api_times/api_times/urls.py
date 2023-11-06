from django.urls import path
from gerar_times import views

urlpatterns = [
    path('gerar_time/<int:tamanho>/', views.gerar_time_api, name='gerar_time_api'),
    path('salvar_dados_aluno/', views.salvar_dados_aluno, name='salvar_dados_aluno'),
    path('salvar_dados_professor/', views.salvar_dados_professor, name='salvar_dados_professor'),
    path('listar_alunos/', views.listar_alunos, name='listar_alunos'),
]
