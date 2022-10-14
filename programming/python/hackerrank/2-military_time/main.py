'Challenge problem to convert AM/PM time to military time'

MY_TIME = '11:55:45pm'


def military_time(my_time: str) -> str:
    'Function to convert normal time to military time'
    am_pm = my_time[-2:]
    if am_pm.upper() == 'PM':
        if my_time[:2] == '12':
            new_time = f"12{my_time[2:-2]}"
        else:
            new_time = f"{str(int(my_time[:2]) + 12)}{my_time[2:-2]}"
    else:
        if my_time[:2] == '12':
            new_time = f"00{my_time[2:-2]}"
        else:
            new_time = my_time[:-2]
    return new_time


print(military_time(MY_TIME))
