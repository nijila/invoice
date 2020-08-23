# Django rest framework
from rest_framework import serializers

# local
from ..models import Invoice


class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoice
        fields = (
            'id',
            'invoice_num',
            'client_name',
            'client_email',
            'project_name',
            'Amount',
        )