# Write code below 💖

import random

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)

total = die1 + die2 

while total!=2:
  print("Nope")
  die1 = random.randint(1, 6)
  die2 = random.randint(1, 6)
  total=die1+die2
  if total == 2:
    print('Snake eyes')
