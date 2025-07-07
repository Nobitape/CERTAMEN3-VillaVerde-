from rest_framework import permissions

class EsJuntaDeVecinos(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.user and request.user.is_superuser:
            return True
        return request.user.groups.filter(name='Junta de Vecinos').exists()
