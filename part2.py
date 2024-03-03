current_time = int(input('current time: '))
time_till_alarm = int(input('how long until alarm goes off?: '))

current_time += time_till_alarm


while(current_time > 24):
    current_time -= 24


print(current_time)