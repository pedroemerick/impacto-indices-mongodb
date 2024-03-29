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
db = client['cindices']
collection = db['data']

# Criação do indice
collection.create_index([("temperature", pymongo.ASCENDING)])

insercao_com_indice = 0
geracao_dados = 0

actual_days = 1

disk_usage_before = util.diskUsage()
usage_stats = util.usageStats(actual_days, "stats_com_indice.csv")

# Inserção de N documentos
qnt_blocks = int(TOTAL_DATA / NUM_CITIES) + 2
for ii in range(1, qnt_blocks):
    if ((ii*NUM_CITIES) / 1440000) > actual_days:
        # Busca sem indice
        inicio = timeit.default_timer()
        search = collection.find({"temperature": {"$lte": 15}})

        # Apenas para ter um cálculo mais preciso do tempo
        for item in search:
            pass

        fim = timeit.default_timer()
        busca_com_indice = fim - inicio

        usage_stats.kill()

        disk_usage_after = util.diskUsage()
        disk_usage_total = disk_usage_after - disk_usage_before

        tempo_total = geracao_dados + insercao_com_indice + busca_com_indice

        with open("./data/tempo_com_indice.csv", "a") as f:
            times = str(actual_days) + ","
            times += str(geracao_dados) + ","
            times += str(insercao_com_indice) + ","
            times += str(busca_com_indice) + ","
            times += str(tempo_total) + ","
            times += str(NUM_DATA_PER_DAY * actual_days * NUM_CITIES) + ","
            times += str(disk_usage_total) + "\n"
            f.write(times)

        print("-> Finished - %i day(s)" % actual_days)  

        actual_days += 1
        usage_stats = util.usageStats(actual_days, "stats_com_indice.csv")    

    inicio = timeit.default_timer()
    data = util.generateData()
    fim = timeit.default_timer()
    geracao_dados += (fim - inicio)

    inicio = timeit.default_timer()
    collection.insert_many(data)
    fim = timeit.default_timer()
    insercao_com_indice += (fim - inicio)

usage_stats.kill()
exit()