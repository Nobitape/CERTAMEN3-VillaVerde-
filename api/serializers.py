from rest_framework import serializers
from talleres.models import Taller

class TallerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taller
        fields = '__all__'
        read_only_fields = ['estado', 'observacion', 'propuesto_por']