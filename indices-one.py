from pymongo import MongoClient
import pymongo
import random
import timeit

NUM_INSERTIONS = 1000000

# Conexão com o mongo e seleção de database e collection
client = MongoClient('localhost', 27017)
db = client['test-indices']
collection = db['indices']

# Inserção de N documentos
inicio = timeit.default_timer()
for ii in range(NUM_INSERTIONS):
    vals = {
        "val1":random.randint(0, 100),
        "val2":random.randint(0, 100)
    }

    collection.insert_one(vals)
fim = timeit.default_timer()
insercaoSemIndice = fim - inicio

# Busca sem indice
inicio = timeit.default_timer()
search = collection.find({"val1": {"$lte": 10}})

# Apenas para ter um cálculo mais preciso do tempo
for item in search:
    pass

fim = timeit.default_timer()
buscaSemIndice = fim - inicio

# Criação de indice
collection.create_index([("val1", pymongo.ASCENDING)])

# Busca com indice
inicio = timeit.default_timer()
search = collection.find({"val1": {"$lte": 10}})

# Apenas para ter um cálculo mais preciso do tempo
for item in search:
    pass

fim = timeit.default_timer()
buscaComIndice = fim - inicio

# Busca com indice e projeção
inicio = timeit.default_timer()
search = collection.find({"val1": {"$lte": 10}}, {"_id":0, "val2":0})

# Apenas para ter um cálculo mais preciso do tempo
for item in search:
    pass

fim = timeit.default_timer()
buscaComIndiceProjecao = fim - inicio

# Drop na coleção e criação do indice novamente
collection.drop()
collection.create_index([("val1", pymongo.ASCENDING)])

# Inserção de N documentos com indice
inicio = timeit.default_timer()
for ii in range(NUM_INSERTIONS):
    vals = {
        "val1":random.randint(0, 100),
        "val2":random.randint(0, 100)
    }

    collection.insert_one(vals)
fim = timeit.default_timer()
insercaoComIndice = fim - inicio

print("-> Inserção: %.6f" % insercaoSemIndice)
print("-> Busca sem indice: %.6f" % buscaSemIndice)
print("-> Busca com indice: %.6f" % buscaComIndice)
print("-> Busca com indice e projeção: %.6f" % buscaComIndiceProjecao)
print("-> Inserção com indice: %.6f" % insercaoComIndice)