## 리스트에 있는 키의 평균 구하기

student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0   ##값 초기화
for height in student_heights:   ##student_heights 리스트의 키 값 가져와
  total_height += height     ##키 값이 저장된 height를 total_height에 추가
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
  number_of_students += 1   ##students_heights에서 항목 가져올 때마다 1씩 증가
print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students)   #round()함수로 정수 만들기
print(f"average height = {average_height}")