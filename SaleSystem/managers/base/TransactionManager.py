from django.db import models

from SaleSystem.models.items.tickets.TicketVariant import TicketVariant


class TransactionManager(models.Manager):
   def create_ticket_transaction(self, request):
      user   = request.user
      request_data   =  request.POST
      ticket = TicketVariant.objects.get_proper_variant(request_data['price'])

      if ticket.is_profile_needed:
         user.profile.

      if request_data['payment_gateway'] == 'Przelewy24':



      selected_variant     =  request_data['selected_variant']
      buyer_comment        =  request_data['buyer_comment']