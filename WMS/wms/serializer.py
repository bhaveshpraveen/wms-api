from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Reading

class ReadingSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Reading
        fields = ('temperature', 'pressure', 'updated', 'owner')
        read_only_fields = ('updated',)
