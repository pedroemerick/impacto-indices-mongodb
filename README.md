## Teste de performance do uso de índices

Os resultados dos testes são de execuções dos programas em um computador com a seguinte configuração:

* Sistema Operacional: Ubuntu 18.04.3 LTS
* Processador: AMD® A8-5500b apu with radeon(tm) hd graphics × 4
* Mémoria RAM: 8 GB
* Tipo de sistema: 64-bit

---

### Teste 1 *(indices-one.py)*

O primeiro teste gera o dado e o insere, ou seja, inserção um a um, isto 1 milhão de vezes. É importante lembrar que neste caso o tempo de inserção inclui o tempo para geração do dado.

#### Resultados (em segundos) do teste 1:

* Inserção: 843.904847
* Busca sem indice: 1.389988
* Busca com indice: 1.158223
* Busca com indice e projeção: 0.938344
* Inserção com indice: 920.313364

---

### Teste 2 *(indices-many.py)*

Após o primeiro teste, decidi testar a inserção de vários documentos ao mesmo tempo, para isso, no inicio do programa é gerada uma lista com 1 milhão de dados, e esta lista é usada para a inserção. Nos resultados a seguir podemos ver que com a inserção de todos os documentos ao mesmo tempo, a diferença de tempo é muito grande.

#### Resultados (em segundos) do teste 2:

* Geração dos 1000000 dados: 5.059150
* Inserção: 29.956600
* Busca sem indice: 1.356378
* Busca com indice: 1.084300
* Busca com indice e projeção: 0.955855
* Inserção com indice: 27.700094