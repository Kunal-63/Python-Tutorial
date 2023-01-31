# Some important modules:
# datetime module
# import datetime
"""
print(dir(datetime))
# print(datetime.MAXYEAR)
# print(datetime.MINYEAR)

last_lecture = datetime.date(2022, 7, 1)
# print(last_lecture)
# print(last_lecture.year)
# print(last_lecture.month)
# print(last_lecture.day)

valentines_day = datetime.date(2023, 2, 14)
chandrayaan2 = datetime.date(2019, 7, 22)
gap = valentines_day - chandrayaan2
# print(gap)
twinkle = datetime.datetime(2007, 10, 5, 17, 30, 15)
todays_date = datetime.datetime.now()
print(todays_date)
print("Your age in days =", todays_date - twinkle)

time1 = datetime.time(20, 45)
print(time1)

interval = datetime.timedelta(100)

print("target date =", todays_date + interval)

# 20 Oct 2021 at 05:45
# Sunday, Oct 20th 2021 at 05:45am
# moon_mission = datetime.datetime(2021, 10, 20, 5, 45)
# print(moon_mission)
# formatted_date = datetime.datetime.strftime(moon_mission, "%A, %b %dth %Y at %I:%M %p")
# print(formatted_date)

# date_from_user = "October 21st, Thu in 2021 at 16:30"
# obj = datetime.datetime.strptime(date_from_user, "%B %dst, %a in %Y at %H:%M")
# print(obj)
"""
"""
import time

# print(time.time())
# print(dir(time))
# print(time.gmtime())
t1 = time.time()
def rec_fib(n):
    if n<=1:
        return n
    else:
        return  rec_fib(n-1)+rec_fib(n-2)

print("No.\tTerm")
for i in range(1, 31):
    print(f"{i}\t{rec_fib(i)}")
t2 = time.time()
exe_time = t2 - t1
print(exe_time)
"""
# Memoization - Explicit
"""
cache_memory = {}
# cache_memory = {1:1, 2:1, 3:2, 4:3, }
def rec_fib(n):
    if n in cache_memory.keys():
        return cache_memory[n]
    if n<=1:
        cache_memory[n] = n
        return n
    else:
        term = rec_fib(n-1)+rec_fib(n-2)
        cache_memory[n] = term
        return term

print("No.\tTerm")
for i in range(1, 1000):
    print(f"{i}\t{rec_fib(i)}")
"""
# Implicit Memoization
"""
from functools import lru_cache

@lru_cache(maxsize=1000)
def rec_fib(n):
    if n<=1:
        return n
    else:
        return  rec_fib(n-1)+rec_fib(n-2)

print("No.\tTerm")
for i in range(1, 1001):
    print(f"{i}\t{rec_fib(i)}")
"""
# Next Lecture: timeit & random module