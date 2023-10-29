from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework import viewsets, status
from dashboard.models import Nuson
from .serializers import NusonSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404




class NusonViewSet(viewsets.ModelViewSet):
    queryset = Nuson.objects.all()
    serializer_class = NusonSerializer

    @api_view(['GET'])
    def add(request):
        if request.method == 'GET':
            nilai1 = request.GET.get('nilai1')
            nilai2 = request.GET.get('nilai2')
            nilai3 = request.GET.get('nilai3')
            nilai4 = request.GET.get('nilai4')
            nilai5 = request.GET.get('nilai5')
            device_name = request.GET.get('deviceName')

            nuson_data = {
                'nilai1': nilai1,
                'nilai2': nilai2,
                'nilai3': nilai3,
                'nilai4': nilai4,
                'nilai5': nilai5,
                'deviceName': device_name,
            }
            
            serializer = NusonSerializer(data=nuson_data)

            if serializer.is_valid():
                serializer.save()
                return redirect(reverse('index'))
                # return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['DELETE'])
    def delete_data(request, pk):
        data = get_object_or_404(Nuson, pk=pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

























