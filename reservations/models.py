from django.db import models

from django.db import models

class Table(models.Model):

    SECTION_CHOICES = [
        ('indoor', 'Indoor'),
        ('patio', 'Patio'),
    ]

    name = models.CharField(max_length=10)
    section = models.CharField(max_length=10, choices=SECTION_CHOICES)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.section}, {self.capacity}-top)"


class Reservation(models.Model):

    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('seated', 'Seated'),
        ('done', 'Done'),
        ('noshow', 'No-show'),
    ]

    guest_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    party_size = models.IntegerField()
    contact = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='upcoming'
    )
    table = models.ForeignKey(
        Table,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='reservations'
    )

    def __str__(self):
        return f"{self.guest_name} — {self.date} at {self.time}"