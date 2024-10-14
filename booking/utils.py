from .models import Table, Booking
from datetime import datetime, timedelta


def find_available_table(date, time, guests):
    print('FINDING TABLES...')
    # Find all tables that can accommodate the number of guests
    suitable_tables = Table.objects.filter(
        capacity__gte=guests).order_by('capacity')

    print('TABLES: ', suitable_tables)
    for table in suitable_tables:
        # Check if there are any bookings for this table at the specified date
        print('TABLE ', table, '\n')
        existing_bookings = Booking.objects.filter(table=table, date=date)
        requested_datetime = datetime.combine(date, time)
        if not any(
            abs((datetime.combine(booking.date, booking.time) -
                 requested_datetime).total_seconds()) < 3600
            for booking in existing_bookings
        ):
            return table

    return None  # No suitable table available
