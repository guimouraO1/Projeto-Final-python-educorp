import json
from datetime import datetime, timedelta
import logging

###########################################################################
#     Script que lê arquivo .json e retorna IDs válidos para execução     #
###########################################################################
#  Metodo:                                                                #
#  Descricao: Script que lê arquivo .json e retorna IDs válidos para      #
#  execução  depedendo da data e hora                                     #
#  Autor: Guilherme de Moura Oliveira  <guimoura@unicamp.br>              #
#  Data: 30/06/2023                                                       #
#  Atualizacao:                                                           #
###########################################################################

caminho_arquivo = 'jobs.json'
arq_log = 'logs/Projeto_Final_.log'

logging.basicConfig(filename=arq_log, level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", datefmt="%d/%m/%Y %H:%M:%S")


logging.info('')
logging.info('')
logging.info('==================================================================================================================')
logging.info('                                INICIO        verificando o arquivo                                               ')
logging.info('==================================================================================================================')
logging.info('')
logging.info('')

try:
    with open(caminho_arquivo, 'r') as arquivo_json:
        dados_lidos = json.load(arquivo_json) 
        logging.info(f'O arquivo {arquivo_json} foi aberto com sucesso.')
        logging.info('')
        # print(dados_lidos[0]["Janela de execução"]) 
        janela_execucao = dados_lidos[0]["Janela de execução"] # atribuindo a key Janela de execução a var janela_execução que retorta 2022-07-04 00:00:00 até 2022-07-09 00:00:00
        logging.info(f'Extraindo Janela de execução')
        logging.info('')
        
        # partindo a string da janela_execução em 2 dividindo pelo "até" ficando data_inicio = 2022-07-04 00:00:00; data_fim = 2022-07-09 00:00:00
        data_inicio, data_fim = janela_execucao.split(" até ")
        
        ids_validos_para_ex = []
       
        for job in dados_lidos[0]['lista']:
            
            logging.info('')
            logging.info('Verificando IDs e datas para confirmar se é possível a execução no tempo determinado')
            logging.info('')
            
            data_conclusao = job['Data Máxima de conclusão']  # data máxima que fica em lista[{data máxima de conclusão}]
            # print(type(data_conclusao))
            
            t_estimado_horas = job['Tempo estimado'] # tempo a mais para a execução que também deve ser levado em conta
            tempo_estimado, excluir_horas = t_estimado_horas.split(' horas') # tirando as horas do tempo estimado pois da erro
           
            data_formatada = datetime.strptime(data_conclusao, '%Y-%m-%d %H:%M:%S') # usando o strptime para poder fazer a soma das duas horas a mais
            # print(type(data_formatada))
            
            data_nova = data_formatada + timedelta(hours=int(tempo_estimado))  # somando tempo estimado com a data extraida,
            # lembrando que utilizei int para tranformar o tempo estimado em inteiro pq ele veio como string assim dnado erro na execução
            
            data_nova_formatada = datetime.strftime(data_nova, "%Y-%m-%d %H:%M:%S") # data que vai ser passada no final 
            logging.info('')
            logging.info(f'ID: {job["ID"]}')
            logging.info(f'Data prevista para execução {data_conclusao}')
            logging.info(f'Data prevista para execução + tempo de execução {data_nova_formatada}')
            logging.info(f'Data máxima para o código ter sido executado {data_fim}')
            
            if datetime.strptime(data_inicio, "%Y-%m-%d %H:%M:%S") <= datetime.strptime(data_nova_formatada, "%Y-%m-%d %H:%M:%S") <= datetime.strptime(data_fim, "%Y-%m-%d %H:%M:%S"):
                ids_validos_para_ex.append(job["ID"])
                logging.info(f'ID: {job["ID"]} Consegue rodar a tempo até o final da data fim')
                logging.info('')
            else:
                logging.info('Não pode ser executado pois passou do tempo limite')
                
                
        print(f'Ids que passaram na verificação e podem ser executados: {ids_validos_para_ex}')
        logging.info(f'Ids que passaram na verificação e podem ser executados: {ids_validos_para_ex}')

except Exception as error:
    print(f'Erro ao abrir o arquivo {caminho_arquivo}: {str(error)}')
    logging.info(f'Erro ao abrir o arquivo {caminho_arquivo}: {str(error)}')
    

logging.info('')
logging.info('')
logging.info("==================================================================================================================")
logging.info("=                                                     FIM                                                        =")
logging.info("==================================================================================================================")
logging.info('')
logging.info('')
    
