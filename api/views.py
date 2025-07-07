from rest_framework import viewsets, permissions
from talleres.models import Taller
from api.serializers import TallerSerializer
from .permissions import EsJuntaDeVecinos
from rest_framework.permissions import IsAuthenticated

class TallerViewSet(viewsets.ModelViewSet):
    queryset = Taller.objects.all()
    serializer_class = TallerSerializer
    permission_classes = [IsAuthenticated, EsJuntaDeVecinos]

    def perform_create(self, serializer):
        serializer.save(propuesto_por=self.request.user, estado='pendiente')
        