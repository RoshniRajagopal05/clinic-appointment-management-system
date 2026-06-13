from rest_framework import serializers
from accounts.models import User


class ReceptionistSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password'
        ]

    def create(self, validated_data):

        password = validated_data.pop('password')

        user = User(
            role='RECEPTIONIST',
            **validated_data
        )

        user.set_password(password)
        user.save()

        return user