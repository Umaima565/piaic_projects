import time
import os


def countdown(t):
  while t:
    mins, secs = divmod(t, 60)
    timer = "{:02d}:{:02d}".format(mins, secs)

    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(timer)
    time.sleep(1)
    t -= 1

  print("Countdown completed!!")

t = input("Enter time in seconds: ")
countdown(int(t))