from datetime import datetime

runs = 99999
i = 0
start = datetime.now().microsecond

while i < runs:
    i += 2
    i -= 1

end = datetime.now().microsecond
timetaken = end-start
print(timetaken)
print(str(timetaken/1000)+"ms")

