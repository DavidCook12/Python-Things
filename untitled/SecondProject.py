r = str(input("What's your name? "))
b = str(input("How old are you? "))
c = str(input("What's your favorite color? "))
w = str(input("Are you happy right now? "))

print("Your answers were:", r + ",", b + ",", c + ",", w)
Join = input('Is this what you said?')
if Join.lower() == 'yes':
  print("Great,", r + '!')
else:
  print ("Hmmm, not good...")
