from rest_framework.routers import DefaultRouter
from api.views import TallerViewSet

router = DefaultRouter()
router.register(r'talleres', TallerViewSet, basename='taller')

urlpatterns = router.urls