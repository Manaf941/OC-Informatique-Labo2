# this version is roughly 5.5x times faster than exo4.randint.py
# For an even more optimized version (Python is slow)
# see src/main.rs (in Rust)
# or exo4.random.mjs (in Javascript, ran by https://bun.sh)

# exo4.rs has multithreading, bitwise operations
# and is written in Rust (which is significantly faster
# than Python, since it's native code)

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

maxn = 2**1024
for i in range(0, throws, 1024):
    # Python has been performing faster with
    # strings operations than with bits operations
    result = format(
        random.randint(0, maxn),
        "b"
    ).rjust(1024, "0")

    for char in result:
        if char == "0":
            heads += 1
        else:
            tails += 1  

duration = time.time() - start

def get_percent(val: int):
    return str(
        round(
            val/(heads+tails)*100,
            # 6 decimals
            6
        )
    ) + "%"


print("Heads:", heads, "Tails:", tails, "Throws:", heads+tails)
print("Heads:", get_percent(heads), "Tails:", get_percent(tails), "Throws:", heads+tails)
print("Duration:", round(duration, 6), "seconds")