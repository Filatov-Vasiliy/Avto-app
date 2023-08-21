from rest_framework.viewsets import ReadOnlyModelViewSet

from api.serializers import AdSerializer, MarkaSerializer
from api.models import Ad


class AdViewSet(ReadOnlyModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
