import random
with open("mrn.txt", "w") as f:
    for i in range(1000):
        f.write(",".join(f"{random.randint(1000,9999)}" for _ in range(random.randint(1,10))) + '\n')
