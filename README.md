### Introdução
Esse repositório tem o objetivo de analisar o impacto dos índices no MongoDB ao escalar uma aplicação em um contexto com dados meteorológicos. Iremos trabalhar com inserção, busca e armazenamento com e sem índices, monitorando os recursos computacionais (memória, cpu e disco). O MongoDB estava sendo executado em um container Docker.

### Estrutura
Os arquivos que compõem experimento são:
* **sem_indices.py**: executa os testes sem o uso de índices;
* **com_indices.py**: executa os testes com o uso de índices;
* **util.py**: funções auxiliares utilizadas pelos programas **sem_indices.py** e **com_indices.py**;
* **data**: diretório com os resultados dos programas e comandos executados.

### Configuração
Os resultados dos testes são de execuções dos programas em um computador com a seguinte configuração:
* Sistema Operacional: Deepin 15.11
* Processador: Intel(R) Core(TM) CPU @ 1.70GHz x 4
* Mémoria RAM: 8 GB
* Tipo de sistema: 64-bit
* Armazenamento: HD de 500 GB

### Documentação
Os resultados do experimento foi documentado e anlisado em forma de um post no Medium e pode ser acessado por esse link: https://medium.com/@valmircsjr/impacto-dos-%C3%ADndices-no-mongodb-9d8cb134138c
