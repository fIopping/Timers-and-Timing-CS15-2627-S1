import time
import random
# Set start_time to the current time
start_time = time.monotonic()

# Define how long the timer should run for
timer_length = random.choice([2,5])

times = []

for i in range(5):
    timer_length = random.choice([2, 5])
    time.sleep(timer_length)
    print("Go")
    # Update the current_time
    start_time = time.monotonic()
    answer = input()
    end_time = time.monotonic()

    times.append(end_time - start_time)
    print(f"{end_time - start_time} seconds")
smallest = min(times)
print(f"Your fastest time was {smallest} seconds")




