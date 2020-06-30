from django.db import models
from Service.models import Image
from SaleSystem.models.items.tickets import TicketVariant


class TicketPrize(models.Model):
    name                =   models.CharField(max_length=20)
    description         =   models.CharField(max_length=100)
    main_image          =   models.OneToOneField(Image, on_delete=models.CASCADE)
    qty                 =   models.IntegerField(null=True)

    available_in_ticket_variants    =   models.ManyToManyField(TicketVariant, related_name="available_prizes")
