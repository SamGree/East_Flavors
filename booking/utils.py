from .models import Table, Booking
from datetime import datetime, timedelta, timezone as datetime_timezone
from datetime import datetime
from pytz import timezone, utc


def find_available_table(date, time, guests, user, tzname):
    print('FINDING TABLES...')

    requested_datetime = datetime.combine(date, time)
    one_hour = timedelta(hours=1)

    print(requested_datetime)
    local_tz = timezone(tzname or "UTC")
    local_aware_datetime = local_tz.localize(requested_datetime)

    # Convert the timezone-aware datetime to UTC
    utc_datetime = local_aware_datetime.astimezone(utc)

    print('utc', utc_datetime)
    if utc_datetime < datetime.now(datetime_timezone.utc):
        return None
    # Check if the user already has any booking within 1 hour before
    # or after the requested time
    user_booking_conflict = Booking.objects.filter(
        user=user,
        date=date,
        # Any booking 1 hour before
        time__gte=(requested_datetime - one_hour).time(),
        # Any booking 1 hour after
        time__lte=(requested_datetime + one_hour).time()
    ).exists()

    if user_booking_conflict:
        return None  # T

    # Find all tables that can accommodate the number of guests
    suitable_tables = Table.objects.filter(
        capacity__gte=guests).order_by('capacity')

    print('TABLES: ', suitable_tables)
    for table in suitable_tables:
        # Check if there are any bookings for this table at the specified date
        print('TABLE ', table, '\n')
        print(user)
        existing_bookings = Booking.objects.filter(
            table=table, date=date)
        requested_datetime = datetime.combine(date, time)

        if not any(
            abs((datetime.combine(booking.date, booking.time) -
                 requested_datetime).total_seconds()) < 3600
            for booking in existing_bookings
        ):
            return table

    return None  # No suitable table available
