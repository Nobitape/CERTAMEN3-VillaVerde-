from rest_framework import viewsets, permissions
from talleres.models import Taller
from api.serializers import TallerSerializer

class TallerViewSet(viewsets.ModelViewSet):
    queryset = Taller.objects.all()
    serializer_class = TallerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(propuesto_por=self.request.user, estado='pendiente')