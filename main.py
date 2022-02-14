class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


# quests
daily = ['Do 3 lists of exercises', 'Study for 3 hours', 'Watch the classes']
weekly = ['Do 15 lists of exercises', 'Study for 15 hours']
monthly = ['Do 60 lists of exercises', 'Study for 60 hours']


daily_1 = 0
daily_2 = 0
daily_3 = False

weekly_1 = 0
weekly_2 = 0

monthly_1 = 0
monthly_2 = 0


def check_done_day(num):
    if num == 0:
        if daily_1 >= 3:
            return '✔'
        else:
            return '❌'
    elif num == 1:
        if daily_2 >= 3:
            return '✔'
        else:
            return '❌'
    elif num == 2:
        if daily_3:
            return '✔'
        else:
            return '❌'
    else:
        pass


def check_done_week(num):
    if num == 0:
        if daily_1 >= 15:
            return '✔'
        else:
            return '❌'
    elif num == 1:
        if daily_2 >= 15:
            return '✔'
        else:
            return '❌'
    else:
        pass


def check_done_month(num):
    if num == 0:
        if daily_1 >= 60:
            return '✔'
        else:
            return '❌'
    elif num == 1:
        if daily_2 >= 60:
            return '✔'
        else:
            return '❌'
    else:
        pass


def print_text():
    global daily, weekly, monthly
    print('Your quests are: ')
    print(color.BOLD + '\nDaily\n' + color.END)
    for items in range(len(daily)):
        checkbox = check_done_day(items)
        print(f'{checkbox} {daily[items]}')

    print(color.BOLD + '\nWeekly\n' + color.END)
    for items in range(len(weekly)):
        checkbox = check_done_week(items)
        print(f'{checkbox} {weekly[items]}')

    print(color.BOLD + '\nMonthly\n' + color.END)
    for items in range(len(monthly)):
        checkbox = check_done_month(items)
        print(f'{checkbox} {monthly[items]}')


print_text()
