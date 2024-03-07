stacks = int(input("how tall (1 ~ 8) should the pyramid be? "))
if stacks < 1 or stacks > 8:
  print("sorry, that's out of range.")
  exit()
for i in range(stacks):
  for j in range(stacks):
    if j > i:
      print(' ', end='')
  for k in range(stacks):
      if k <= i:
        print('#', end='')
  print()