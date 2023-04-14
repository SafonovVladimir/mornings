def make_readable(seconds: int) -> str:
    hours = seconds // 3600
    minutes = seconds % 3600 // 60
    seconds = seconds - hours * 3600 - minutes * 60
    return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

    # time.strftime('%H:%M:%S', time.gmtime(seconds))
    # return time.strftime('%H:%M:%S', time.gmtime(seconds))


print(make_readable(0))  # повертає "00:00:00"
print(make_readable(5))  # повертає "00:00:05"
print(make_readable(60))  # повертає "00:01:00"
print(make_readable(359999))  # повертає "99:59:59"
