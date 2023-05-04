import datetime

weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

date_str = input("Enter a date (dd/mm/yyyy): ")

date_obj = datetime.datetime.strptime(date_str, "%d/%m/%Y")
day_of_week = date_obj.weekday()

print(weekday_names[day_of_week])
