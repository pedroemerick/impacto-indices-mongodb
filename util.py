from datetime import datetime
import random
import subprocess

def generateData():
    NUM_CITIES = 1000
    cities = []
    for ii in range(NUM_CITIES):
        city = {}
        city['city'] = "city" + str(int(ii))
        city['state'] = "state" + str(int(ii/100))
        city['country'] = "BR"
        
        cities.append(city)

    data = []
    for city in cities:
        # for ii in range(NUM_DATA_PER_CITY):
        info = {}
        info['temperature'] = random.randint(0, 40)
        info['location'] = city
        info['datetime'] = datetime.now().isoformat()

        data += [info]

    return data

def diskUsage():
    # "0d739e3dec15d0a84918b0a1e889db63cde44916d0ebbfe15947ef7c0be58e3d",
    volumes = ["e5e3c7fbe7ecd09cb575f19772a2d8699c021bd3c1dfc9c1219a4cff92ad0dc2"]

    for volume in volumes:
        cmd = 'docker system df -v | grep '
        cmd += volume
        cmd += ' | cut -d" " -f23'

        usage = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        usage.wait()

        usage_value_str = usage.stdout.read().decode("utf-8")
        usage_value_str = usage_value_str[:-1]
        
        if usage_value_str[-2:] == "GB":
            usage_value = float(usage_value_str[:-2]) * 1000
        else:
            usage_value = float(usage_value_str[:-2])
        
        return usage_value

def usageStats(days):
    cmd = 'while true; do { { echo '
    cmd += str(days)
    cmd += '; date +%d/%m/%y-%T; } | tr "\n" ","; '
    cmd += 'docker stats --no-stream '
    cmd += '--format "{{.Container}},{{.CPUPerc}},{{.MemUsage}},{{.MemPerc}},{{.BlockIO}}" mongo;  }; '
    cmd += 'sleep 10; done >> ./data/stats_sem_indice.csv'

    usage = subprocess.Popen(cmd, shell=True, stdout=None)

    return usage