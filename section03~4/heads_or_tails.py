#앞면 혹은 뒷면 중 랜덤하게 출력하기

import random

random_coin = random.randint(0, 1)
if random_coin == 1 :
  print("Heads")
else :
  print("Tails")