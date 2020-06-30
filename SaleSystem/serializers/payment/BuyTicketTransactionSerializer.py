from rest_framework import serializers
from SaleSystem.settings import *
from SaleSystem.models.payment.Przelewy24 import Przelewy24


class BuyTicketTransactionSerializer(serializers.Serializer):
        price           =   serializers.FloatField(required=True)
        buyer_comment   =   serializers.CharField(max_length=500)
        fighter_code    =   serializers.CharField(max_length=10)
        profile         =   ProfileSerializer(required=False)


        def is_request_valid(self, raise_exception=False):
            if self.price == None:
                raise serializers.ValidationError("Ticket price can't be none")

            if self.price == None:
                raise serializers.ValidationError("Ticket price must be positive")

            if self.price < MINIMAL_TICKET_PRICE:
                raise serializers.ValidationError(f"Ticket price must be higher than MINIMAL_TICKET_PRICE (Current: {MINIMAL_TICKET_PRICE})")

            ## if fighter code correct

            return self.is_valid(raise_exception=raise_exception)


