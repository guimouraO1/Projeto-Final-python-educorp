from funcoes import logging_inicio as inicio, config_log as config, logging_fim as fim, abrir_arquivo, janela_execucao, verificacao, log_ids_validos as ids_validos

###########################################################################
#     Script que lê arquivo .json e retorna IDs válidos para execução     #
###########################################################################
#  Metodo:                                                                #
#  Descricao: Script que lê arquivo .json e retorna IDs válidos para      #
#  execução  dentro da janela de execução                                 #
#  Autor: Guilherme de Moura Oliveira  <guimoura@unicamp.br>              #
#  Data: 30/06/2023                                                       #
#  Atualizacao: 05/07/2023                                                #
###########################################################################

# caminho do arquivo
caminho_arquivo = 'jobs.json'

# configurando log
config()

# log início
inicio()

# abrindo o arquivo json por parametro e atribuindo a var dados lidos
dados_lidos = abrir_arquivo(caminho_arquivo)

# atribuindo as variavel janela_exec dos dados lidos: 2022-07-04 00:00:00 até 2022-07-09 00:00:00
janela_exec = janela_execucao(dados_lidos)

# partindo a string da janela_exec em 2 dividindo pelo "até" ficando data_inicio = 2022-07-04 00:00:00; data_fim = 2022-07-09 00:00:00;
data_inicio, data_fim = janela_exec.split(" até ")

# verificando se o job está dentro da janela de execução e retornando os ids válidos
ids_validos_para_ex = verificacao(dados_lidos, data_inicio, data_fim)

# printando ids válidos e colocando no log
ids_validos(ids_validos_para_ex)

# log fim
fim()
