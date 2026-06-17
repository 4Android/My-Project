def get_lastday(num_month, first_day, length_day):
    days = 30 + (num_month + (num_month//8)) % 2
    temp_days = first_day + length_day
    NUM_MONTH = 12

    if num_month == 2:
        days -= 2

    day_overflow = int(temp_days > days)

    last_day = (temp_days - (days * day_overflow)) - 1
    last_month = num_month + day_overflow

    month_overflow = int(last_month > NUM_MONTH)
    last_month = last_month - (NUM_MONTH * month_overflow)
    return (last_month, last_day)

num_month = int(input("Enter a number of month: "))
first_day = int(input("Enter first day: "))
length_day = int(input("Enter length of day: "))

last_month, last_day = get_lastday(num_month, first_day, length_day)
print(f'Last Month: {last_month}, Last Day: {last_day}')




