# For a faster and improved version, please look at exo4.optimized.py

import random
import time

# ask the user the number of throws
throws = int(input("Throw(s): "))
if throws < 1:
    print("The number must be superior or equal to 1")
    exit(1)

start = time.time()
heads = 0
tails = 0

# for each throw, get either 0 or 1 from randint and increase counter accordingly
# 0 is heads, 1 is tails
for i in range(0, throws):
    if random.randint(0, 1) == 0:
        heads += 1
    else:
        tails += 1

duration = time.time() - start

def get_percent(val: int):
    return str(
        round(
            val/throws*100,
            # 6 decimals
            6
        )
    ) + "%"


print("Heads:", heads, "Tails:", tails, "Throws:", throws)
print("Heads:", get_percent(heads), "Tails:", get_percent(heads), "Throws:", throws)
print("Duration:", round(duration, 6), "seconds")