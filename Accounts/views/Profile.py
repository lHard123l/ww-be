from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from django.contrib.auth.models import User
from Accounts.serializers.ProfileSerializer import ProfileSerializer
from Accounts.models.Profile import Profile as ProfileModel


class Profile(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)

    def get(self, request, format=None):
        if request.user.is_authenticated:
            profile = ProfileModel.objects.get(user=request.user.id)
            profile_serializer = ProfileSerializer(profile, many=False)
        return Response(profile_serializer.data)

    def post(self, request, format=None):
        if request.user.is_authenticated:
            profile_serializer      =   ProfileSerializer(data=request.data)
            if profile_serializer.is_valid():
                profile_serializer.save()
                print(profile_serializer.data)
            return Response(profile_serializer.data, status=status.HTTP_201_CREATED)

