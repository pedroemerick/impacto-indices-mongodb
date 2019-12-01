from pymongo import MongoClient
from datetime import datetime
import pymongo
import random
import timeit
import json
import sys
import pickle

import util

NUM_DAYS = int(sys.argv[1])
NUM_CITIES = 1000
NUM_DATA_PER_DAY = 24*60
TOTAL_DATA = NUM_DATA_PER_DAY * NUM_DAYS * NUM_CITIES

# Conexão com o mongo e seleção de database e collection
client = MongoClient('localhost', 27017)
db = client['sem-indices']
collection = db['data']

disk_usage_before = util.diskUsage()
usage_stats = util.usageStats(NUM_DAYS)

# Inserção de N documentos
insercaoSemIndice = 0
geracaoDados = 0

qnt_blocks = int(TOTAL_DATA / NUM_CITIES)
for ii in range(qnt_blocks):
    inicio = timeit.default_timer()
    data = util.generateData()
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

usage_stats.kill()

disk_usage_after = util.diskUsage()
disk_usage_total = disk_usage_after - disk_usage_before

with open("./data/tempo_sem_indice.csv", "a") as f:
    times = str(NUM_DAYS) + ","
    times += str(geracaoDados) + ","
    times += str(insercaoSemIndice) + ","
    times += str(buscaSemIndice) + ","
    times += str(TOTAL_DATA) + ","
    times += str(disk_usage_total) + "\n"
    f.write(times)