from django.db import models
from django.utils import timezone

from Accounts.models import User
from SaleSystem.enums.TicketStatus import TicketStatus
from SaleSystem.enums.TransactionStatus import TransactionStatus
from SaleSystem.models.items.tickets import TicketVariant
from Service.models.base import Event




class Ticket(models.Model):
    price               =   models.FloatField(null=False)
    additional_data     = models.CharField(max_length=500, null=True)
    player_token        = models.CharField(max_length=100, null=True)

    selected_variant    =   models.ForeignKey(TicketVariant, on_delete=models.DO_NOTHING, null=False)
    buyer               =   models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False)
    event               =   models.ForeignKey(Event, on_delete=models.DO_NOTHING, null=False)


    @property
    def status(self):
        if self.transaction.status != TransactionStatus.FINALIZED:
            return TicketStatus.NEW

        if self.player_token == None:
            return TicketStatus.PENDING

        if  self.event.start_time > timezone.now:
            return TicketStatus.ACCEPTED

        if self.event.start_time < timezone.now and self.event.start_time > timezone.now:
            return TicketStatus.ACTIVE

        if self.event.end_time < timezone.now:
            return TicketStatus.OUTDATED
