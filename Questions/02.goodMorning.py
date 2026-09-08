'''Write a python program capable of greeting you good morning, good afternoon and good night'''
import time
time1=int(time.strftime('%H'))
name=input("Enter your username: ")
if(time1>=00 and time1<=11):
    print(f"Hello, {name} good morning")
elif(time1>=12 and time1<=4):
    print(f"Hello, {name} good afternoon")
else:
    print(f"Hello, {name} good evening")