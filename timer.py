import time  
import os  
def countdown(t):
    """
    Countdown function that takes time in seconds (t)
    and prints the remaining time in MM:SS format.
    """
    while t:
        mins, secs = divmod(t, 60)  # Convert total seconds to minutes and seconds
        timer = "{:02d}:{:02d}".format(mins, secs)  # Format the time as MM:SS

        os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen for updated display

        print(timer)  # Show the current countdown time
        time.sleep(1)  # Pause for 1 second
        t -= 1  # Decrease time by 1 second

    print("Countdown completed!!")  # Notify when countdown ends

# Get user input for countdown duration
t = input("Enter time in seconds: ")  
countdown(int(t))  # Start countdown
