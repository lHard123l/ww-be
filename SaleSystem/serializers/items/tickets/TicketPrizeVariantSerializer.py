from rest_framework import serializers

from Service.models import Image
from SaleSystem.models.items.tickets import TicketPrizeVariant


class TicketPrizeVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model       = TicketPrizeVariant
        fields      = ['id', 'name', 'description', 'main_image', 'qty']


