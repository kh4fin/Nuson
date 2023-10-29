from django.shortcuts import render
from .models import Nuson


def index(request):
    datas = Nuson.objects.all().order_by('-waktu')[:8]
    return render(request, 'dashboard/index.html', {'datas':datas})

def statistik(request):
    datas = Nuson.objects.all().order_by('-waktu')[:8]
    return render(request, 'statistik/index.html', {'datas':datas})



