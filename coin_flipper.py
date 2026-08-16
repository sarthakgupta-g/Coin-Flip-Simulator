import random

heads=0
tails=0
coins_flipped=0

total_flips=int(input("how many coins do you wish to flip"))

while(coins_flipped<total_flips):
  coin=random.choice(["heads","tails"])
  coins_flipped+=1
  if(coin=="heads"):
    heads+=1
  else:
    tails+=1

print(f"heads={heads}")
print(f"tails={tails}")
