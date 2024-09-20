min = int(input())

count = 0
min_count = 0
time = 1200

def counting():
    global time, count, min_count, min
    while min_count <= min:
        _time = list(str(time))
        for i in range(len(_time)):
            _time[i] = int(_time[i])

        if _time[0] == 0:
            _time.pop(0)
        if len(_time) == 3:
            if _time[0] - _time[1] == _time[1] - _time[2]:
                count += 1
        else:
            if _time[0] - _time[1] == _time[1] - _time[2] == _time[2] - _time[3]:
                count += 1

        if len(_time) == 3:
            _time[2] += 1
            if _time[2] == 10:
                _time[2] = 0
                _time[1] += 1
            if _time[1] == 6:
                _time[1] = 0
                _time[0] += 1
            if _time[0] == 13:
                _time[2] = 0
                _time[1] = 0
                _time[0] = 1
        if len(_time) == 4:
            _time[3] += 1
            if _time[3] == 10:
                _time[3] = 0
                _time[2] += 1
            if _time[2] == 6:
                _time[2] = 0
                _time[1] += 1
            if _time[1] == 10:
                _time[1] = 0
                _time[0] += 1
            if _time[0] == 1 and _time[1] == 3:
                _time[3] = 0
                _time[2] = 0
                _time[1] = 1
                _time[0] = 0

        for i in range(len(_time)):
            _time[i] = str(_time[i])
        time = ''.join(_time)

        min_count += 1


if min < 720:
    counting()
else:
    half_days = min // 720
    # Every 12 hours there are 31 arithmetic sequence times
    count += half_days * 31
    min -= half_days * 720
    counting()

print(count)