
import os
import random

used_random = []

os.chdir("aPredic")
for filename in os.listdir():
    n = random.randint(1, len(os.listdir()))
    while n in used_random:
        n = random.randint(1, len(os.listdir()))
    used_random.append(n)
    os.rename(filename, f"{n}_{filename}")