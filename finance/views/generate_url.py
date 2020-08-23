# 3rd party
from rest_framework import viewsets

# local
from ..models import Invoice
from ..serializers import GenrateUrlSerializer


class GenerateUrlViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = GenrateUrlSerializer