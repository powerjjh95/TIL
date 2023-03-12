hour, minute = map(int, input().split())

if hour == 0 and minute < 45:
    hour = 23
    minute = minute + 60 - 45
elif hour == 0 and minute >= 45:
    minute -= 45
elif 0 < hour <= 23 and minute < 45:
    hour -= 1
    minute = minute + 60 - 45
else:
    minute -= 45

print(hour, minute)