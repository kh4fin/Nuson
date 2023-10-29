from rest_framework import serializers
from dashboard.models import Nuson

class NusonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nuson
        fields = '__all__' 



