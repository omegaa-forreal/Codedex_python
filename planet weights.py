# Write code below 💖

erwg = float(input('What is your earth weight? '))
num = int(input('Choose a planet by its number: '))



if num == 1:
  Mercury = erwg*0.38
  print('Your weight will be ',Mercury)
elif num == 2:
  Venus = erwg*0.91
  print('Your weight will be ',Venus)
elif num == 3:
  Mars = erwg*0.38
  print('Your weight will be ',Mars)
elif num == 4:
  Jupiter = erwg*2.53
  print('Your weight will be ',Jupiter)
elif num == 5:
  Saturn = erwg*1.07
  print('Your weight will be ',Saturn)
elif num == 6: 
  Uranus = erwg*0.89
  print('Your weight will be ',Uranus)
elif num == 7:
  Neptune =erwg*1.14
  print('Your weight will be ',Neptune)
else:
  print('Invalid number')
