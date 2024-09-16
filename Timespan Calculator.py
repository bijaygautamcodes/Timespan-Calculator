from datetime import datetime, timedelta

def calculate_timespan(start_date):
    # Current date
    current_date = datetime.now()
    
    # Calculate the difference in years, months, and days
    years = current_date.year - start_date.year
    months = current_date.month - start_date.month
    days = current_date.day - start_date.day

    # Adjust if the days are negative
    if days < 0:
        months -= 1
        previous_month_end = (current_date.replace(day=1) - timedelta(days=1)).day
        days += previous_month_end

    # Adjust if the months are negative
    if months < 0:
        years -= 1
        months += 12
    
    return years, months, days

# List of start dates
dates = [
    datetime(2001, 10, 1), # Birth
    datetime(2018, 3, 31), # SEE Completed
    datetime(2020, 12, 1), # +2 Completed
    datetime(2023, 8, 27) # Bachelors Completed
]

# Calculate and print the timespan for each date
for date in dates:
    years, months, days = calculate_timespan(date)
    print(f"From {date.strftime('%Y/%m/%d')} to today: {years} Years, {months} Months, {days} Days")
