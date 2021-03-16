duration = input('Введите число секунд: ')
duration = int(duration)
if duration <= 59:
    print(duration, 'сек')
elif duration >= 60 and duration <= 3599:
    duration_minute = duration // 60
    duration_seconds = duration % 60
    print(duration_minute, 'минут', duration_seconds, 'секунд')
elif duration >= 3600:
    duration_hour = duration // 3600
    duration_minute = duration % 3600 // 60
    duration_seconds = duration % 60
    print(duration_hour, 'час', duration_minute, 'минут', duration_seconds, 'секунд')
