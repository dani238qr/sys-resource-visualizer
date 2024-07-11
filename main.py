import os
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from datetime import datetime

#file
mem_file="memory.txt"
pack_file="packages.txt"

#commands for memory and packages
mem_command ='df -h /dev/sda2'
pack_command ='dpkg --get-selections | wc --lines'

#command to get data
data_command='date "+%e %b %H:%M"'

#run commands and append to file
os.system(f'{mem_command} >> {mem_file}')
os.system(f'{data_command} >> {mem_file}')

os.system(f'{pack_command} >> {pack_file}')
os.system(f'{data_command} >> {pack_file}')

#make list
pack_list=[]
mem_list=[]
time_list=[]


with open("packages.txt","r") as rd:
    data=rd.readlines()
    for i in range(len(data)):
        if i%2==0:
            pack_list.append(int(data[i].strip()))
        else:
            time_list.append(data[i].strip())

with open("memory.txt","r") as fd:
    mem_data=fd.readlines()
    for i in range(len(mem_data)):
        if mem_data[i][0]=='/':
            mem_list.append(mem_data[i].strip())
    

capacities = []
used = []
free = []

for entry in mem_list:
    parts = entry.split()
    capacities.append(int(parts[1][:-1]))
    used.append(int(parts[2][:-1]))  
    free.append(int(parts[3][:-1])) 

#print(mem_list)
#print(capacities)
#print(used)
#print(free)


#format data ( day, month, hour and minute)
date_format = '%d %b %H:%M'
dates = [datetime.strptime(ts, date_format) for ts in time_list]

plt.figure(figsize=(10, 6))

plt.plot(dates, capacities, marker='o', linestyle='-', color='b', label='Capacity (G)')
plt.plot(dates, used, marker='o', linestyle='-', color='r', label='Used (G)')
plt.plot(dates, free, marker='o', linestyle='-', color='g', label='Free (G)')

plt.title('Disk Usage Over Time')
plt.xlabel('Timestamp')
plt.ylabel('Size (G)')

plt.legend()

date_form = DateFormatter('%d %b %H:%M')
plt.gca().xaxis.set_major_formatter(date_form)

plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

#plt.show()


plt.figure(figsize=(10, 6))
plt.plot(dates, pack_list, marker='o', linestyle='-', color='b')

#plt.bar(dates,pack_list, color='skyblue')

plt.title('Package Counts Over Time')
plt.xlabel('Timestamp')
plt.ylabel('Package Count')


date_form = DateFormatter('%d %b %H:%M')
plt.gca().xaxis.set_major_formatter(date_form)

plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.show()  


