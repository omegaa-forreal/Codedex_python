guess = 0
tries = 0
while guess != 6 and tries<5:
  guess = int(input("Guess the number:  "))
  tries=tries+1
print("You got it!")