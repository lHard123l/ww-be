from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User


class BuyTicketTransactionView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        if request.user.has_ticket:
            return {"has_ticket": True}
        return {"has_ticket": False}



    def post(self, request, format=None):
        ticket_value = request.POST.value
