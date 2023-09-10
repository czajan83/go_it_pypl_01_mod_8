from datetime import datetime

users = [{"name": "Andrzej", "birthday": datetime(1983, 10, 27)},
         {"name": "Marta", "birthday": datetime(2000, 9, 9)},
         {"name": "Aldona", "birthday": datetime(2000, 9, 10)},
         {"name": "Michal", "birthday": datetime(2000, 9, 11)},
         {"name": "Wiktoria", "birthday": datetime(2000, 9, 12)},
         {"name": "Wladek", "birthday": datetime(2000, 9, 13)},
         {"name": "Iga", "birthday": datetime(2000, 9, 14)},
         {"name": "Tadek", "birthday": datetime(2000, 9, 15)},
         {"name": "Artur", "birthday": datetime(2000, 9, 16)},
         {"name": "Kamila", "birthday": datetime(2000, 9, 4)},
         {"name": "Natalia", "birthday": datetime(2000, 9, 3)},
         {"name": "Zuzia", "birthday": datetime(2000, 9, 19)}]

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


def get_usernames_list_from_dict(users_dict):
    current_year = datetime.today().year
    current_day = datetime.today().timetuple().tm_yday
    last_day_this_year = datetime(current_year, 12, 31).timetuple().tm_yday
    users_names = []
    days_deltas = []
    for user in users_dict:
        users_names.append(user["name"])
        day_delta = user["birthday"].timetuple().tm_yday - current_day - 1
        if day_delta < -2:
            day_delta += last_day_this_year
        days_deltas.append(day_delta)
    return users_names, days_deltas


def get_names_this_week(usernames, day_deltas, offset, next_day_week):
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


def get_birthdays_per_single_week(week, users_names, days_deltas):
    this_day_week = datetime.today().weekday()
    result = f"{week} week:\n"
    next_day_week = 0
    if week == f"This":
        next_day_week = this_day_week
    shift = 7 - this_day_week
    if week == f"This":
        shift = 0
    offset = 0
    while next_day_week < 5:
        result += f"{weekdays[next_day_week]}: " \
                  f"{get_names_this_week(users_names, days_deltas, offset + shift, next_day_week)}\n"
        offset += 1
        next_day_week += 1
    return result


def get_birthday_per_week():
    users_names, days_deltas = get_usernames_list_from_dict(users)
    print(get_birthdays_per_single_week(f"This", users_names, days_deltas))
    print(get_birthdays_per_single_week(f"Next", users_names, days_deltas))


if __name__ == "__main__":
    get_birthday_per_week()
