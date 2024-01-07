from datetime import datetime, timedelta

def generate_time_intervals(start_datetime, end_datetime):
    current_datetime = start_datetime

    while current_datetime <= end_datetime:
        yield current_datetime
        current_datetime += timedelta(minutes=1)

# Example Usage:
s_date_str = "2024-01-01 12:00:00"
e_date_str = "2024-01-02 12:00:00"

s_datetime = datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S")
e_datetime = datetime.strptime(end_date_str, "%Y-%m-%d %H:%M:%S")

for time_interval in generate_time_intervals(s_datetime, e_datetime):
    print(time_interval)