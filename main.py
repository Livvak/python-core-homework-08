from datetime import date, datetime, timedelta
from collections import defaultdict


def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання

    today_date = date.today()
    current_year = today_date.year
    # current_week = today_date + timedelta(days=6)
    users_list = defaultdict(list)

    if not users:
        return {}

    # Визначаємо потрібний період (тиждень)
    begin_data = date.today()
    end_data = begin_data + timedelta(days=6)

    for user in users:
        name = user['name']
        birthday = user['birthday']
        if birthday.month == 1:
            birthday_this_year = birthday.replace(year=current_year + 1)
        else:
            birthday_this_year = birthday.replace(year=current_year)

        if begin_data <= birthday_this_year <= end_data:    #  потрібний нам період

            if birthday_this_year < today_date:
                continue

            if birthday_this_year.weekday() >= 5:
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))

            day_name = birthday_this_year.strftime('%A')
            imya = user["name"].split(' ')[0]
            users_list[day_name].append(imya)

    return users_list


if __name__ == "__main__":
    # users = [
    #     {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    # ]

    users = [
        {"name": "Jan0110 Koum", "birthday": datetime(1976, 10, 1).date()},
        {"name": "Vase2410 Koum", "birthday": datetime(1976, 10, 24).date()},
        {"name": "Ritu2909 Koum", "birthday": datetime(1976, 9, 29).date()},
        {"name": "Koum3009 Ntyu", "birthday": datetime(1977, 9, 30).date()},
        {"name": "Faser0410 Koum", "birthday": datetime(1970, 10, 4).date()},
        {"name": "Oppens2911 Deft", "birthday": datetime(1970, 11, 29).date()},
        {"name": "Bobbi2709 Ritu", "birthday": datetime(1971, 9, 27).date()},
        {"name": "Luj0612 Kid", "birthday": datetime(1980, 12, 6).date()},
        {"name": "Aysew0310 Fret", "birthday": datetime(1979, 10, 3).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
