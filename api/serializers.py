from rest_framework import serializers
from talleres.models import Taller

class TallerSerializer(serializers.ModelSerializer):
    profesor = serializers.SerializerMethodField()
    lugar = serializers.SerializerMethodField()
    categoria = serializers.SerializerMethodField()

    class Meta:
        model = Taller
        fields = [
            'id', 'titulo', 'fecha', 'duracion_horas', 'estado',
            'observacion', 'profesor', 'lugar', 'categoria'
        ]
        read_only_fields = ['estado', 'observacion', 'propuesto_por']

    def get_profesor(self, obj):
        return obj.profesor.nombre_completo

    def get_lugar(self, obj):
        return obj.lugar.nombre

    def get_categoria(self, obj):
        return obj.categoria.nombre