# import the time module
import time

my_time=int(input("pls enter your time(seconds): "))
for x in range(my_time,0,-1):
    second= x%60
    minutes=int(x/60)%60
    hours=int(x/3600)
    print(f"{hours:02}:{minutes:02}:{second:02}")
    time.sleep(1)
print("Vaxt bitdi!!!")
