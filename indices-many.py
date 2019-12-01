from pymongo import MongoClient
from datetime import datetime
import pymongo
import random
import timeit
import json
import sys
import pickle

import disk_usage
import generate_data
from pymongo.errors import BulkWriteError

NUM_DAYS = int(sys.argv[1])
NUM_CITIES = 1000
NUM_DATA_PER_DAY = 24*60
TOTAL_DATA = NUM_DATA_PER_DAY * NUM_DAYS * NUM_CITIES

# Conexão com o mongo e seleção de database e collection
client = MongoClient('localhost', 27017)
db = client['test']
collection = db['test']

disk_usage.saveDiskUsage("./data/fs_sem_indice.csv", "antes de inserir - 1 dia")

# Inserção de N documentos
insercaoSemIndice = 0
geracaoDados = 0

qnt_blocks = int(TOTAL_DATA / NUM_CITIES)
for ii in range(qnt_blocks):
    inicio = timeit.default_timer()
    data = generate_data.generateData()
    fim = timeit.default_timer()
    geracaoDados += (fim - inicio)

    inicio = timeit.default_timer()
    collection.insert_many(data)
    fim = timeit.default_timer()
    insercaoSemIndice += (fim - inicio)

# Busca sem indice
inicio = timeit.default_timer()
search = collection.find({"temperature": {"$lte": 15}})

# Apenas para ter um cálculo mais preciso do tempo
for item in search:
    pass

fim = timeit.default_timer()
buscaSemIndice = fim - inicio

disk_usage.saveDiskUsage("./data/fs_sem_indice.csv", "depois de inserir - 1 dia")

# # Criação de indice
# collection.create_index([("val1", pymongo.ASCENDING)])

# # Busca com indice
# inicio = timeit.default_timer()
# search = collection.find({"val1": {"$lte": 10}})

# # Apenas para ter um cálculo mais preciso do tempo
# for item in search:
#     pass

# fim = timeit.default_timer()
# buscaComIndice = fim - inicio

# # Busca com indice e projeção
# inicio = timeit.default_timer()
# search = collection.find({"val1": {"$lte": 10}}, {"_id":0, "val2":0})

# # Apenas para ter um cálculo mais preciso do tempo
# for item in search:
#     pass

# fim = timeit.default_timer()
# buscaComIndiceProjecao = fim - inicio

# # Drop na coleção e criação do indice novamente
# collection.drop()
# collection.create_index([("val1", pymongo.ASCENDING)])

# # Inserção de N documentos com indice
# inicio = timeit.default_timer()
# collection.insert_many(data)
# fim = timeit.default_timer()
# insercaoComIndice = fim - inicio

print("-> Geração dos %i dados: %.6f" % (TOTAL_DATA, geracaoDados))
print("-> Inserção: %.6f" % insercaoSemIndice)
print("-> Busca sem indice: %.6f" % buscaSemIndice)
# print("-> Busca com indice: %.6f" % buscaComIndice)
# print("-> Busca com indice e projeção: %.6f" % buscaComIndiceProjecao)
# print("-> Inserção com indice: %.6f" % insercaoComIndice)