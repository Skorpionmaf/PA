import calendar

def first_bisestile(x):
    if calendar.isleap(x) == False:
        x = first_bisestile(x+1);

    return x;

y = first_bisestile(2015)    
print(y)

l = list(map(calendar.isleap, [x for x in range(2000, 2051)]))
count = 0;
for x in l: count+=(1 if x else 0)
print(count)

l = "Jul 29 2016".split()
mesi = {"Jan":1, "Feb":2 , "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Set":9, "Oct":10, "Nov":11, "Dec":12}
d = calendar.weekday(int(l[2]), mesi[l[0]], int(l[1]))
print(d)

