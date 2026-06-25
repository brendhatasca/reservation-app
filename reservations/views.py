from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Table, Reservation
from .serializers import TableSerializer, ReservationSerializer

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all().order_by('name')
    serializer_class = TableSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer

    def get_queryset(self):
        queryset = Reservation.objects.all().order_by('date', 'time')
        date = self.request.query_params.get('date')
        if date:
            queryset = queryset.filter(date=date)
        return queryset