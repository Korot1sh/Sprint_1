times = '1h 45m,360s,25m,30m 120s,2h 60s'
total_time = 0
time_values = times.split(',')
#print(time_values)
for value in time_values:
    value = value.replace(' ', '')
    if 'h' in value:
        hours = int(value.split('h')[0])
        total_time += hours * 60
        value = value.split('h', 1)[1]
        #print(value)
    if 'm' in value:
        minutes = int(value.split('m')[0])
        total_time += minutes
        value = value.split('m', 1)[1]
    if 's' in value:
        seconds = int(value.split('s')[0])
        total_time += seconds // 60
print(total_time)

