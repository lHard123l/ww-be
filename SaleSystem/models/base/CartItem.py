from django.db import models
from SaleSystem.models.items.Product import Product


class CartItem(models.Model):
    product         =   models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity        =   models.IntegerField()


    @property
    def cost_netto(self):
        return int(self.quantity) * float(self.product.price_netto)
    @property
    def cost_brutto(self):
        return int(self.quantity) * float(self.product.price_brutto)

    def free(self):
        self.delete()