import random

for i in range(0, 7):
    if (i == 0):
        lotto_list = set()
    lotto_list.add(random.randrange(1, 45))

print(lotto_list)
