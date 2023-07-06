import logging
import json
from datetime import datetime, timedelta

# Configura o log
def config_log():
    arq_log = 'logs/Projeto_Final_.log'
    logging.basicConfig(filename=arq_log, level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", datefmt="%d/%m/%Y %H:%M:%S")
    
# log início
def logging_inicio():
    
    logging.info('')
    logging.info('')
    logging.info('==================================================================================================================')
    logging.info('                                INICIO        verificando o arquivo                                               ')
    logging.info('==================================================================================================================')
    logging.info('')
    logging.info('')
    
# log fim
def logging_fim():
    
    logging.info('')
    logging.info('')
    logging.info("==================================================================================================================")
    logging.info("=                                                     FIM                                                        =")
    logging.info("==================================================================================================================")
    logging.info('')
    logging.info('')
    
# abrindo o arquivo json por parametro
def abrir_arquivo(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r') as arquivo_json:
            dados_lidos = json.load(arquivo_json)
            logging.info('')
            logging.info(f'O arquivo {arquivo_json} foi aberto com sucesso. ')
            logging.info('')
            return dados_lidos
        
    except Exception as error:
        print(f'Erro ao abrir o arquivo {caminho_arquivo}: {str(error)}')
        logging.info('')
        logging.info(f'Erro ao abrir o arquivo {caminho_arquivo}: {str(error)}')
        logging.info('')
        
        return print(f'Erro ao abrir o arquivo {caminho_arquivo}: {str(error)}')

# Extraindo Janela de execução  2022-07-04 00:00:00 até 2022-07-09 00:00:00
def janela_execucao(dados_lidos):
    
    janela_execucao = dados_lidos[0]["Janela de execução"]
    logging.info('')
    logging.info(f'Extraindo Janela de execução')
    logging.info('')

    return janela_execucao

# Verificar os dados lidos e retornar somente a lista dos ids válidos
def verificacao(dados_lidos, data_inicio, data_fim):
    
    # Criando lista que vai ficar os IDs que passaram na verificação
    ids_validos_para_ex = []
    
    logging.info('')
    logging.info('Verificando IDs e datas para confirmar se é possível a execução no tempo e data determinados')
    logging.info('')
        
    for job in dados_lidos[0]['lista']:
        
        # data máxima que fica em lista[{data máxima de conclusão}]  # print(type(data_conclusao))
        data_conclusao = job['Data Máxima de conclusão']  
        
        # tempo a mais para a execução que também deve ser levado em conta
        t_estimado_horas = job['Tempo estimado']
        
        # tirando as horas do tempo estimado pois da erro
        tempo_estimado = t_estimado_horas.replace(' horas', '') 

        # usando o strptime para transformar em um obj para adicionar abaixo data + hora a mais.  # print(type(data_formatada))
        data_formatada = datetime.strptime(data_conclusao, '%Y-%m-%d %H:%M:%S') 
        
        # somando tempo estimado com a data extraida,
        data_nova = data_formatada + timedelta(hours=int(tempo_estimado))
        
        # imprimindo informações como o ID e a Data Máxima de conclusão
        logging.info('')
        logging.info(f'ID: {job["ID"]}')
        logging.info(f'Data prevista para execução {data_conclusao}.')
        
        # verificando se a data nova que é o calculo total está entre data inicio e data fim. E salvando os IDs que passaram na lista ids válidos para execução
        if datetime.strptime(data_inicio, "%Y-%m-%d %H:%M:%S") <= data_nova <= datetime.strptime(data_fim, "%Y-%m-%d %H:%M:%S"):
            ids_validos_para_ex.append(job["ID"])
            logging.info(f'O job ID: {job["ID"]} Consegue rodar entre a janela de execução com sucesso! ')
            logging.info('')
        else:
            logging.info(f'O job ID:{job["ID"]} NÃO consegue rodar entre a janela de execução.')
            logging.info('')
    # retornando os ids válidos      
    return ids_validos_para_ex

# imprrmindo os ids válidos e salvando no log
def log_ids_validos(ids_validos_para_ex):

    print(f'Ids que passaram na verificação e podem ser executados: ID: {ids_validos_para_ex}')
    logging.info('')
    logging.info(f'Ids que passaram na verificação e podem ser executados dentro da janela de execução: ID(s): {ids_validos_para_ex}')
    logging.info('')