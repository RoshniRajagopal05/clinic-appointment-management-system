from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import (
    ListCreateAPIView
)

from accounts.models import User
from accounts.serializers.user_serializer import UserSerializer
from accounts.serializers.receptionist_serializer import ReceptionistSerializer

from accounts.permissions import IsAdmin


class CurrentUserView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        serializer = UserSerializer(
            request.user
        )

        return Response(
            serializer.data
        )


class ReceptionistListCreateView(
    ListCreateAPIView
):

    serializer_class = (
        ReceptionistSerializer
    )

    permission_classes = [
        IsAdmin
    ]

    def get_queryset(self):

        return User.objects.filter(
            role='RECEPTIONIST'
        )