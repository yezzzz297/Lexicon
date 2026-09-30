def valid_date(date):
    # Use one format so the same date always looks the same.
    if len(date) != 10:
        return False
    if date[4] != "-" or date[7] != "-":
        return False

    year_text = date[0:4]
    month_text = date[5:7]
    day_text = date[8:10]

    for character in year_text + month_text + day_text:
        if character not in "0123456789":
            return False

    year = int(year_text)
    month = int(month_text)
    day = int(day_text)

    if year < 1 or month < 1 or month > 12:
        return False

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # February has 29 days in a leap year.
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        days_in_month[1] = 29

    if day < 1 or day > days_in_month[month - 1]:
        return False

    return True
