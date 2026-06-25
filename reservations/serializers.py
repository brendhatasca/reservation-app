from rest_framework import serializers
from .models import Table, Reservation

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    table_name = serializers.CharField(
        source='table.name',
        read_only=True
    )

    class Meta:
        model = Reservation
        fields = '__all__'