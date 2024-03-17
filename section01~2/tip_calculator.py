#팁 계산기

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))  #숫자로 만들어야 하므로 float로 변환
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))  #마찬가지로 숫자로 만들기 위해 int로 변환
people = int(input("How many people to split the bill?"))

bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person, 2)  #소수점 둘째자리에서 반올림

print(f"Each person should pay: ${final_amount}")

#https://repl.it/@alqkf/tip-calculator-start?embed=1&output=1#main.py