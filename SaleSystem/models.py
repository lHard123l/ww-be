from django.db import models
from django_enum_choices.fields import EnumChoiceField
from SaleSystem.enums import TransactionStatus, TicketStatus
from django.core.exceptions import ObjectDoesNotExist
# Create your models here.
from SaleSystem.models.base import Transaction


class Ticket(models.Model):
    comments        =   models.TextField(default="")
    event_no        =   models.IntegerField(default=6)
    token           =   models.TextField(null=True)  ##TO JWT

    @property
    def is_paid(self):
        try:
            with Transaction.objects.get(products__ticket=self) as related_transaction:
                if related_transaction.status == TransactionStatus.FINALIZED:
                    return True
        except ObjectDoesNotExist:
            print(f"DATABASE ERROR: THERE IS NO TRANSACTION RELATED TO TICKET ID:{self.id}")
        return False


    @property
    def status(self):
        if not self.is_paid:
            return TicketStatus.NEW
        if self.token != None:
            return TicketStatus.ACTIVE
        return TicketStatus.PENDING




class ProductImage(models.Model):
    img             =   models.ImageField(null=True, upload_to="D:/")

class Product(models.Model):
    name            =   models.CharField(max_length=200, default="")
    description     =   models.TextField(default="")
    cost            =   models.FloatField(default=0)
    needs_profile   =   models.BooleanField(default=False)
    main_image      =   models.OneToOneField(ProductImage, null=True, on_delete=models.CASCADE, related_name='MainImage')  #check
    images          =   models.ForeignKey(ProductImage, null=True, on_delete=models.CASCADE, related_name='Images')  #check


class Item(models.Model):
    product         =   models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    amount          =   models.IntegerField(default=1)
    transaction     =   models.ForeignKey(Transaction, on_delete=models.DO_NOTHING)
    value           =   models.FloatField(default=0)
