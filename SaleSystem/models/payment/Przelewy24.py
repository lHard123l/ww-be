from SaleSystem.models.base.Transaction import Transaction
from django_enum_choices.fields import EnumChoiceField
from SaleSystem.enums import PaymentStatus
from django.db import models
from SaleSystem.settings import *
from Accounts.models import User as User
from SaleSystem.managers.payment.PaymentGatewayManager import PaymentGatewayManager

class Przelewy24(models.Model):
    merchant_id     =   models.CharField(max_length=50, null=False)
    pos_id          =   models.CharField(max_length=50, null=False)
    session_id      =   models.CharField(max_length=50, null=False, unique=True)
    amount          =   models.FloatField(null=False)
    currency        =   models.CharField(max_length=3, null=False)
    description     =   models.CharField(max_length=1000, null=False)
    email           =   models.EmailField(null=False)


    client_name     =   models.CharField(max_length=50, null=True)
    address         =   models.CharField(max_length=80, null=True)
    postal_code     =   models.CharField(max_length=10, null=True)
    city            =   models.CharField(max_length=50, null=True)

    country         =   models.CharField(max_length=50, null=False)

    phone_number    =   models.IntegerField(null=True)
    language        =   models.CharField(max_length=12, default="pl")
    method          =   models.IntegerField(null=True)
    url_return      =   models.CharField(max_length=250, null=False)
    url_status      =   models.CharField(max_length=250, null=True)
    timeLimit       =   models.IntegerField(max_length=2, default=0)
    channel         =   models.IntegerField(null=True)
    shipping_cost   =   models.FloatField(null=True)
    transfer_label  =   models.CharField(max_length=20, null=True)
    sign            =   models.CharField(max_length=100, null=False)
    mobile_lib      =   models.IntegerField(null=True)
    sdk_version     =   models.CharField(max_length=10, null=True)
    encoding        =   models.CharField(max_length=15, null=True)
    method_ref_id   =   models.CharField(max_length=250, null=True)

    payment_status  =   EnumChoiceField(PaymentStatus, default=PaymentStatus.NULL)

    transaction     =   models.OneToOneField(Transaction, on_delete=models.DO_NOTHING, related_name="payment")

    def basic_required_data_setup(self):
        pass

    def shipping_data_setup(self):
        pass

    def test_connection(self):
        print(Przelewy24.objects.make_request(PRZELEWY_24_TEST_ACCESS, {}))


    def set_up_payment(self, amount:float, description:str, user:User, currency:str = "PLN", country="PL", language:str="pl"):
        if not self.payment_status == PaymentStatus.NULL:
            print(f"Payment #{self.id} is already set up")
            return None

        if len(description) > 1000:
            description = description[:1000]

        if len(language) > 2:
            language    =   language[:2]

        if len(country) > 2:
            country     =   country[:2]

        self.merchant_id            =   PRZELEWY_24_MERCHANT_ID
        self.pos_id                 =   PRZELEWY_24_MERCHANT_ID
        self.session_id             =   f"Przelewy24#{self.id}"
        self.amount                 =   amount
        self.currency               =   currency
        self.description            =   description
        self.email                  =   user.email
        self.country                =   country.upper()
        self.language               =   language.lower()
        self.url_return             =   PRZELEWY_24_REDIRECT_URL + f"{self.transaction.id}/"
        self.sign                   =   Przelewy24.objects.sign_transaction({"sessionId":f"{self.session_id}", "merchantId":self.merchant_id, "amount":self.amount, "currency":self.currency, "crc":PRZELEWY_24_CRC_KEY})

        self.payment_status         =   PaymentStatus.UNREGISTRED

        print(self.merchant_id, self.url_return, self.sign,self.session_id)



    def register_payment(self):
        if not self.payment_status == PaymentStatus.UNREGISTRED:
            print(f"Payment #{self.id} is already registred in Przelewy24")
            return None

        request_data   =   {}

        request_data["merchantId"]  =   self.merchant_id
        request_data["posId"]       =   self.pos_id
        request_data["sessionId"]   =   self.session_id
        request_data["amount"]      =   self.amount
        request_data["currency"]    =   self.currency
        request_data["description"] =   self.description
        request_data["email"]       =   self.email
        request_data["country"]     =   self.country
        request_data["language"]    =   self.language
        request_data["url_return"]  =   self.url_return
        request_data["sign"]        =   self.sign

        response = Przelewy24.objects.make_request(PRZELEWY_24_URL + PRZELEWY_24_REGISTER_TRANSACTION, request_data)

        if response == None:
            print(f"Payment #{self.id} is already registred in Przelewy24")
            return None
        if response.status != 200:
            print(f"Payment #{self.id} made invalid request")
            return None

        return response

        objects             =   PaymentGatewayManager()

