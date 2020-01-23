import matplotlib.pyplot as plt
from datetime import datetime, timedelta

members = {}

file = open('chat.txt', 'r')
lines = file.readlines()

first_message = datetime(year=2021, month=1, day=1)
last_message = datetime(year=2000, month=1, day=1)

for line in lines:
    if line.__len__() > 17 and line[2] == '/' and line.__contains__(': '):
        time = datetime.strptime(line.split(' - ')[0], '%d/%m/%y, %H:%M')
        first_message = min(time, first_message)
        last_message = max(time, last_message)

        user = line.split(' - ')[1].split(': ')[0]
        if members.__contains__(user):
            members[user].append(time)
        else:
            members[user] = []

resolution = timedelta(hours=int(input()))
x_fact = int((last_message - first_message).total_seconds()/resolution.total_seconds()) + 1
x = [a*resolution.total_seconds()/(3600*24) for a in range(x_fact)]

plt.tight_layout()

for member in members:
    if member[0] != '+':
        y = [0]*x_fact
        for message in members[member]:
            ind = int((message - first_message).total_seconds()/resolution.total_seconds())
            y[ind] += 1
        plt.plot(x, y, label=str(member))

plt.xlabel(str(first_message.date()) + ' to ' + str(last_message.date()))
plt.ylabel('activity')
plt.title('usage')
plt.legend()
plt.show()
