# Write code below 💖
Gryffindor =  0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0
print('===============')
print('The Sorting Hat')
print('===============')

q1 = int(input('Q1 Do you like Dawn or Dusk? 1 Dawn - 2 Dusk :'))
if q1 == 1:
  Gryffindor = Gryffindor +1
  Ravenclaw = Ravenclaw +1
elif q1 == 2:
  Hufflepuff = Hufflepuff+1
  Slytherin = Slytherin+1
else:
  print('Wrong input broski')

q2 = int(input(("When I'm dead, I want people to remember me as: 1 The Good 2 The Great 3 The Wise 4 The Bold: ")))


if q2 == 1:
  Hufflepuff = Hufflepuff +2
elif q2 == 2:
  Slytherin = Slytherin +2
elif q2 == 3:
  Ravenclaw = Ravenclaw +2
elif q2 == 4:
  Gryffindor = Gryffindor +2
else:
  print("wrong input")


q3 = int(input('Which kind of instrument most pleases your ear? 1 violin 2 trumpet 3 piano 4 drum : '))

if q3 == 2:
  Hufflepuff = Hufflepuff +4
elif q3 == 1:
  Slytherin = Slytherin +4
elif q3 == 3:
  Ravenclaw = Ravenclaw +4
elif q3 == 4:
  Gryffindor = Gryffindor +4
else:
  print("wrong input")

print('Hufflepuff',Hufflepuff)
print('Slytherin',Slytherin)
print('Ravenclaw',Ravenclaw)
print('Gryffindor',Gryffindor)
