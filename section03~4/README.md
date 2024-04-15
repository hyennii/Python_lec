## (필기 정리)

1. if else 형식
```python
    if condition :
        do this
    else :
        do this
```

2. elif

    : else if 

3. lower() : 모든 문자를 소문자로 변형
```python
    a = b.lower()
```

4. upper() : 모든 문자를 대문자로 변형

5. random module 사용하기

    ** https://www.askpython.com/

    1)  ```python
            import random
        ```

    2) randint(a,b) 
     
         : a와 b를 포함해 a와 b사이의 정수 난수 반환

    ```python
        random_integer = random.randint(1, 10)  #1이상 10 이하

        print(random_integer)   #1이상 10 이하의 숫자 랜덤으로 출력
    ```

    3) random()

        : 1을 포함하지 않고 0과 1 사이에 존재하는 숫자 출력

    ```python
        random_float = random.random()

        print(random_float)     #0과 1 사이의 부동 소수점 출력
    ```

6. List

    : 대괄호 안에 모든 데이터 형식 저장

    1) list 안에서 특정 순서의 데이터 추출 
    ```python
        fruits = ["apple", "watermelon", "grapes", "mango", "strawberry", "orange"]

        print(fruits[0])      #데이터인덱스로 순서 출력
    ```

    2) 음수를 사용하면 뒤에서부터 시작
    ```python
        fruits = ["apple", "watermelon", "grapes", "mango", "strawberry", "orange"]

        print(fruits[-1])       #orange 출력
    ```

    3) 데이터 변경 가능
    ```python
        fruits = ["apple", "watermelon", "grapes", "mango", "strawberry", "orange"]

        fruits[1] = "cherry"
        print(fruits)        #watermelon 대신 cherry 출력
    ```
    
    4) list의 맨 뒤에 추가
    ```python
        fruits.append("melon")      #append함수 : 항목을 list 마지막에 추가
    ```
         