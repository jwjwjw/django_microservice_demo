from rest_framework import serializers
from .models import Email


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ('sender', 'receiver', 'subject', 'body',)
