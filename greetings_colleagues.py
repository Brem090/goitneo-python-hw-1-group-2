import datetime

def get_birthdays_per_week(users):
    birthdays_per_day = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
    today = datetime.date.today()
    for user in users:
        name = user["name"]
        birthday = user["birthday"]
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)
        delta_days = (birthday_this_year - today).days
        if delta_days < 7:
            day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Monday", "Monday"][birthday_this_year.weekday()]
            birthdays_per_day[day_of_week].append(name)
    result = []
    for day_of_week, names in sorted(birthdays_per_day.items()):
        if names:
            result.append(f"{day_of_week}: {', '.join(names)}")
    
    return result

users = [
    {"name": "Maria Kogut", "birthday": datetime.date(2023, 10, 28)},
    {"name": "Ivan Onishchenko", "birthday": datetime.date(2023, 10, 22)},
    {"name": "Fedir Ivasuk", "birthday": datetime.date(2023, 10, 18)},
    {"name": "Guru Gurienko", "birthday": datetime.date(2023, 10, 16)}
]

birthdays_next_week = get_birthdays_per_week(users)
for birthday in birthdays_next_week:
    print(birthday)