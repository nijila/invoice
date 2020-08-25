# django
from django.db import models
from django.utils import timezone


class Invoice(models.Model):
    """Model definition for Invoice."""

    

    invoice_num = models.CharField('Invoice Number', max_length=150)
    client_name = models.CharField('Client Name', max_length=150)
    client_email = models.EmailField()
    project_name = models.CharField('Project Name', max_length=300)
    Amount =  models.DecimalField('Amount to be Charged',max_digits=12, decimal_places=2, default=0.00)
    payment_status = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now, editable=False)
    

    class Meta:
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'

        

    def __str__(self):
        """Unicode representation of Invoice."""
        return f'{self.invoice_num}'