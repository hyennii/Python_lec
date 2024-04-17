#랜덤 1명이 밥값내기

names = names_string.split(", ")

num_items = len(names)   #names의 list항목 개수 파악
random_choice = random.randint(0, num_items -1)    #인덱스가 0부터 시작하기 때문에 -1, 임의의 숫자얻기
pay_person = names[random_choice]    #임의의 숫자 지정된 random_choice를 list로 넣어 해당하는 이름 가져오기

print(pay_person + ' is going to buy the meal today!')