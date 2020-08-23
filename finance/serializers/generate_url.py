# Django rest framework
from rest_framework import serializers

# local
from ..models import Invoice
from ..serializers import InvoiceSerializer


class GenrateUrlSerializer(serializers.ModelSerializer):
    invoice_number= serializers.CharField(source='invoice_num')
    class Meta:
        model = Invoice
        fields = (
            'invoice_number',
            
        )