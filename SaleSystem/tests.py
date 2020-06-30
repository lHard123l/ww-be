from django.test import TestCase
from Accounts.models import User
from SaleSystem.models.payment.Przelewy24 import Przelewy24
# Create your tests here.

class P24SetUpTest(TestCase):
    def test_setUp(self):
        try:
            if User.objects.get(email="test@test.test") == None:
                user = User.objects.create_user(email="test@test.test", password="test", username="Test")
                user.save()
        except User.DoesNotExist:
            user = User.objects.create_user(email="test@test.test", password="test", username="Test")
            user.save()

    def test_CreatePayment(self):
        payment = Przelewy24.objects.create()
        payment.set_up_payment(100, "Test payment creation", User.objects.get(email="test@test.test"))

