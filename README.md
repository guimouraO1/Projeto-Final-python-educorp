# Trabalho Python Final

Requisitos:

## Excecução do Programa:
Irá rodar em ambientes Linux ou Windows, com o comando: 

```python
python3 [project.py]
```

## Descrição:
Dado um array de "jobs" para execução, no qual cada posição possui um objeto com os seguintes atributos:

1) ID: Identificação do Job;
2) Descrição: Descrição do Job;
3) Data Máxima de conclusão do Job: Data máxima em que o Job deve ser concluído;
4) Tempo estimado: Tempo estimado de execução do Job.

Criar Programa Python que retorne um conjunto de arrays (lista), com as seguintes características:

1) O array contém o conjunto com os números inteiros IDs, que representa uma lista de Jobs a serem executados em sequência;
2) Deve ser respeitada a data máxima de conclusão do Job;
3) Todos os Jobs devem ser executados dentro da janela de execução (data início e fim).

Orientações:

1) Disponibilizar o código final no git e compartilhar o link;
2) Realizar small commits (evitar um commit único com toda a solução);
3) Desenvolver teste automatizado para a solução.

Exemplo de Massa de dados:

```txt
[Janela de execução: 2022-11-10 09:00:00 até 2022-11-11 12:00:00

[
    {
        "ID": 1,
        "Descrição": "Importação de arquivos de fundos",
        "Data Máxima de conclusão": 2022-07-08 23:00:00,
        "Tempo estimado": 2 horas,
    },
    {
        "ID": 2,
        "Descrição": "Importação de dados da Base Legada",
        "Data Máxima de conclusão": 2019-11-11 12:00:00,
        "Tempo estimado": 4 horas,
    },
    {
        "ID": 3,
        "Descrição": "Importação de dados de integração",
          "Data Máxima de conclusão": 2022-11-11 08:00:00,
        "Tempo estimado": 6 horas,
    },
]]
```

Exemplo de output esperado caso da data vigente estaja dentro da data máxima dos IDs 1 e 3:
```txt
[3]
```

Exemplo de caso a data esteja fora da Janela de execução:

```txt
Janela fora do período para execução dos jobs.
```

## Tecnologia(s) e pré-requisitos:
Sistema Operacional: Linux (Preferêncial), mas pode rodar no Windows também.
Liguagem de Programação: Python (versão 3.x)
Pacote e Lib Python: json
