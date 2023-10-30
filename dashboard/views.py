from django.shortcuts import render
from .models import Nuson
import pandas as pd
import pickle
import os
from Nuson.settings import BASE_DIR
import numpy as np

STATIC_DIR = os.path.join(BASE_DIR, 'Nuson\static\modelAi')
test = os.path.join(STATIC_DIR, 'modelRF.pickle')
f = open(test, 'rb')
model = pickle.load(f)
f.close()

def slidingSquence(ddf, idx):
    hasilX = []
    dtX = ddf.iloc[:, :]
    for i in range(0, len(ddf)-idx):
        hasilX.append(np.concatenate(dtX.values[i+1:i+idx+1]))
    return hasilX

def index(request):
    alldata = Nuson.objects.all().order_by('waktu').values("nilai1","nilai2","nilai3","nilai4", "nilai5")
    df = pd.DataFrame(list(alldata), columns=["nilai1","nilai2","nilai3","nilai4", "nilai5"])
    X = slidingSquence(df, 5)
    result = [0, 0, 0, 0, 0]
    for i in X:
        trans = np.array(i).reshape(1, -1)
        result.append(model.predict(trans)[0])

    result = result[::-1] # pembalikan index karena waktu yang berbeda
    # print(result)
    datas = Nuson.objects.all().order_by('-waktu')
    backup = []
    for i, j in enumerate(datas):
        backup.append(j)
        backup[i].label = result[i]
        # print(backup[i])

    # print(datas[0])
    return render(request, 'dashboard/index.html', {'datas':backup})

def statistik(request):
    alldata = Nuson.objects.all().order_by('waktu').values("nilai1","nilai2","nilai3","nilai4", "nilai5")
    df = pd.DataFrame(list(alldata), columns=["nilai1","nilai2","nilai3","nilai4", "nilai5"])
    X = slidingSquence(df, 5)
    result = [0, 0, 0, 0, 0]
    for i in X:
        trans = np.array(i).reshape(1, -1)
        result.append(model.predict(trans)[0])

    result = result[::-1] # pembalikan index karena waktu yang berbeda
    # print(result)
    datas = Nuson.objects.all().order_by('-waktu')
    backup = []
    for i, j in enumerate(datas):
        backup.append(j)
        backup[i].label = result[i]
        # print(backup[i])

    # print(datas[0])
    return render(request, 'statistik/index.html', {'datas':backup},)



