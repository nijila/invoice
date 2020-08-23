from django.contrib import admin

# local
from ..models import Invoice


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    '''Admin View for Invoice'''

    list_display = ('invoice_num','client_name',)
    search_fields = ('invoice_num','client_name',)