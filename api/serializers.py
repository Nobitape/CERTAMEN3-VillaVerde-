from rest_framework import serializers
from talleres.models import Taller

class TallerSerializer(serializers.ModelSerializer):
    profesor_nombre = serializers.SerializerMethodField(read_only=True)
    lugar_nombre = serializers.SerializerMethodField(read_only=True)
    categoria_nombre = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Taller
        fields = [
            'id', 'titulo', 'fecha', 'duracion_horas',
            'estado', 'observacion',
            'profesor', 'profesor_nombre',
            'lugar', 'lugar_nombre',
            'categoria', 'categoria_nombre'
        ]
        read_only_fields = ['estado', 'observacion', 'profesor_nombre', 'lugar_nombre', 'categoria_nombre']

    def get_profesor_nombre(self, obj):
        return obj.profesor.nombre_completo

    def get_lugar_nombre(self, obj):
        return obj.lugar.nombre

    def get_categoria_nombre(self, obj):
        return obj.categoria.nombre


        