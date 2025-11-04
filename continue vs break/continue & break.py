# continue - skips that specific interation and continue the loop
# break - breaks out of the loop entirely

for x in range(1, 21):
    if x % 2 == 0:
        continue
    print(x)