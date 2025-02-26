# 3rd party
from rest_framework import viewsets

# local
from ..models import Invoice
from ..serializers import InvoiceSerializer


class InvoiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer