# 3의 배수에서는 Fizz, 5의 배수에서는 Buzz, 15의 배수에서는 FizzBuzz 출력

target = 100
for number in range(1, target+1):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else :
    print(number)