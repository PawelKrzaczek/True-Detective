def is_twodigit_odd(number):
    return number % 2 == 1 and 10 <= number < 100


def has_access(user, users_groups, file_owner, writable_by_owner, file_group, writable_by_group, writable_by_others, sudo_mode):
    return (user == file_owner and (writable_by_owner or (sudo_mode and (writable_by_group or writable_by_others)))) or (user in users_groups and (writable_by_group or (sudo_mode and writable_by_others))) or (sudo_mode and writable_by_others)


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def is_sunday(day, weekday_of_first):
    return 0 < day <=  31 and (day + ['M', 'Tu', 'W', 'Th', 'F', 'Sa', 'Su'].index(weekday_of_first)) % 7 == 0



def should_bring_umbrella(rains, wind_scale, cloudy, red_sky, strong_flower_smell, spiders_down, lying_cattle, strong_sunshine):
    return wind_scale < 7 and (rains or cloudy and (red_sky or strong_flower_smell or spiders_down or lying_cattle) or strong_sunshine)


def should_take_a_nap(want_to, trouble_sleeping, after_4pm, at_work, mad_boss, have_30m, have_10m):
    return not (not want_to or trouble_sleeping or after_4pm or (at_work and mad_boss)) and (have_10m or have_30m)