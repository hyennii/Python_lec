# 윤년 확인하기

if year % 4 == 0 :
  if year % 100 == 0 :
    if year % 400 == 0 :
      print("Leap year")    # 4, 100, 400 으로 나눴을때 나머지가 없다면 윤년에 해당 
    else :
      print("Not leap year")
  else :
    print("Leap year")    # 100으로 나눌 수 없고, 4로는 나눌 수 있다면 윤년으로 출력
else :
  print("Not leap year")