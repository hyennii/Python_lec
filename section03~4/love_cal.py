print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

# 이름에 포함되어있는 특정 알파벳의 수를 세어, 각각 더한 후
# less than 10 or greater than 90, the message should be: "Your score is *x*, you go together like coke and mentos"
# between 40 and 50, the message should be: "Your score is *y*, you are alright together."
# otherwise, "Your score is *z*."

combined_name = name1 + name2
lower_names = combined_name.lower()
t = lower_names.count('t')
r = lower_names.count('r')
u = lower_names.count('u')
e = lower_names.count('e')
first_digit = t + r + u + e

l = lower_names.count('l')
o = lower_names.count('o')
v = lower_names.count('v')
e = lower_names.count('e')
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))   #단순 +가 아닌, 문자열로 변환하여 + 한 후 숫자끼리 비교해야 하므로 int로 묶어줌

if score < 10 or score > 90 :
    print(f'Your score is {score}, you go together like coke and mentos.')
elif 40 < score < 50 :
    print(f'Your score is {score}, you are alright together.')
else :
    print(f'Your score is {score}.')