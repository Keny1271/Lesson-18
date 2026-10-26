from datetime import date , time , datetime
today = date.today()
now = datetime.now()
print("Today's date is :", today)
print("\nCurrent time is :", now)
print("\nDate components:", now.year, now.month, now.day)