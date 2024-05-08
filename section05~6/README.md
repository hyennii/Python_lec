## (필기 정리)

1. for문 형식

```python
    fruits = ["Apple", "Peach", "Pear"]
    for fruit in fruits:
    print(fruit)    #리스트 반복 실행
```

2. range함수 형식

```python
    for number in range(1, 10, 3):  #1에서10까지의 숫자 범위(10은 미포함) 중 3씩 증가
        print(number)   
```
```python
    #짝수만 더하기(입력한 숫자까지의 짝수)

    target = int(input())

    even_sum = 0

    for number in range(2, target+1, 2) :
    even_sum += number
    print(even_sum)
```

3. 나만의 함수 만들기

```python
    def my_function():  #def : 함수를 생성하거나 정의한다는 의미
        print("Hello")
        print("Bye")

    my_function()   #호출
```




------------------------------------------------------------

- 내장함수 참고 : https://docs.python.org/ko/3/library/functions.html