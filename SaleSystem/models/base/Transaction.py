from django.db import models
from django_enum_choices.fields import EnumChoiceField
from Accounts.models import User as User
from SaleSystem.models.base.CartItem import CartItem


from SaleSystem.enums import TransactionStatus

class Transaction(models.Model):
    user                        =   models.ForeignKey(User, on_delete=models.CASCADE)
    items                       =   models.ForeignKey(CartItem, on_delete=models.SET_NULL, null=True)
    request_time                =   models.DateTimeField(null=True)
    last_status_change_time     =   models.DateTimeField(null=True)
    buyer_comment               =   models.CharField(max_length=1000, null=True)
    status                      =   EnumChoiceField(TransactionStatus, default=TransactionStatus.REQUESTED)

    @property
    def is_paid(self):
        return True

    @property
    def price_netto(self):
        price_netto = 0

        for item in self.items:
            price_netto += item.price_netto
        return price_netto

    @property
    def price_brutto(self):
        price_brutto = 0

        for item in self.items:
            price_brutto += item.price_netto
        return price_brutto


    def request(self):
        pass

    def cancel(self):
        pass

    def refund(self):
        pass

    def validate(self):
        pass

    def add_products_by_id(self):
        pass

    def add_products(self):
        pass

