from datetime import datetime

users = [{"name": "Andrzej", "birthday": datetime(1983, 10, 27)}, {"name": "Marta", "birthday": datetime(2000, 9, 9)},
         {"name": "Aldona", "birthday": datetime(2000, 9, 10)},
         {"name": "Michal", "birthday": datetime(2000, 9, 11)}, {"name": "Wiktoria", "birthday": datetime(2000, 9, 12)},
         {"name": "Wladek", "birthday": datetime(2000, 9, 13)},
         {"name": "Iga", "birthday": datetime(2000, 9, 14)}, {"name": "Tadek", "birthday": datetime(2000, 9, 15)},
         {"name": "Artur", "birthday": datetime(2000, 9, 16)},
         {"name": "Kamila", "birthday": datetime(2000, 9, 4)}, {"name": "Natalia", "birthday": datetime(2000, 9, 3)},
         {"name": "Zuzia", "birthday": datetime(2000, 9, 19)}]

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


def get_weekday_from_datetime(this_date):
    return this_date.weekday()


def take_names_this_week(usernames, day_deltas, offset, next_day_week):
    names = ""
    for index, delta in enumerate(day_deltas):
        if delta == offset:
            names += f"{usernames[index]}, "
        if next_day_week == 0:
            if delta + 1 == offset or delta + 2 == offset:
                names += f"{usernames[index]}, "
    if len(names) > 2:
        names = names[:-2]
    return names


def get_birthday_per_week():
    this_day_year = datetime(2023, 9, 10).timetuple().tm_yday
    this_day_week = datetime(2023, 9, 10).weekday()
    usernames = []
    day_deltas = []
    for user in users:
        usernames.append(user["name"])
        day_deltas.append(user["birthday"].timetuple().tm_yday - this_day_year - 1)
    print(f"This week:")
    next_day_week = this_day_week
    offset = 0
    while next_day_week < 5:
        print(f"{weekdays[next_day_week]}: {take_names_this_week(usernames, day_deltas, offset, next_day_week)}")
        offset += 1
        next_day_week += 1
    print(f"Next week:")
    next_day_week = 0
    offset = 0
    while next_day_week < 5:
        print(
            f"{weekdays[next_day_week]}: {take_names_this_week(usernames, day_deltas, offset + 7 - this_day_week, next_day_week)}")
        offset += 1
        next_day_week += 1


if __name__ == "__main__":
    get_birthday_per_week()
