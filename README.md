### Introducao
Esse repositorio tem o objetivo de analisar o impacto dos índices no MongoDB ao escalar uma aplicação em um contexto com dados meteorológicos. Iremos trabalhar com inserção, busca e armazenamento com e sem índices, monitorando os recursos computacionais (memória, cpu e disco).

### Estrutura
Os arquivos que compoem experimento são:
* **sem_indices.py**: executa os testes sem indices;
* **util.py**: funcçoes uteis utilizadas pelos programas **sem_indices.py** e **com_indices.py**;
* **data**: diretorio com resultados dos programas e comandos executados.

### Configuração
Os resultados dos testes são de execuções dos programas em um computador com a seguinte configuração:
* Sistema Operacional: Ubuntu 18.04.3 LTS
* Processador: AMD® A8-5500b apu with radeon(tm) hd graphics × 4
* Mémoria RAM: 8 GB
* Tipo de sistema: 64-bit

### Documentação
Os resultados do experimento foi documentado e anlisado em forma de um post no Medium e pode ser acessado por esse link: https://medium.com/@valmircsjr/impacto-dos-%C3%ADndices-no-mongodb-9d8cb134138c
