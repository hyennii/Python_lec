## (필기 정리)

1. 줄바꿈 : \n

2. input 함수
   input 함수 사용 시, 출력 함수와 다르게 단어를 입력 받음
   출력 함수 안에 입력함수(input) 실행 시, 받은 내용 출력 가능

    ```python
        print("Hello" + input("What is your name?"))
    ```

3. 주석 : #

4. len() : string 갯수 출력 함수

5. 파이썬에서 \_ 는 무시되지만 사용자에게는 가독성이 좋음

6. type함수 : 데이터 형식 확인

    ex) 정수형에 문자열 형식 추가 불가하여 오류 발생할 때, 데이터 형식을 확인함으로써 원인 파악 가능 

    ```python
        type()
    ```

7. int함수 :  int()를 이용해서 숫자나 문자열을 정수형 (Integer)으로 변환

8. float함수 : float()를 이용해 실수로 변환

9. 나누기 : / 사용하여 나누면 항상 부동 소수점 형태로 출력됨

10. ** : 지수에 곱하거나 숫자의 거듭제곱 표현 가능

    ```python
        2 ** 2  # 결과는 4(= 2*2)
        2 ** 3  # 결과는 8(= 2*2*2)
    ```

11. round함수 : 반올림. 반올림할 자릿수 지정 가능

    ```python
        print(round(8 / 3, 2))  # 소수점 두번째 자리에서 반올림
    ```

12. // : 버림

    ```python
        print(8 // 3)   # 정수 2 출력
    ```

13. 변수 연속으로 사용하기

    ```python
        result = 4 / 2  
        result /= 2
        print(result)   # 1.0 출력
    ```

    ```python
        score = 0
        score +=    # score + 1 과 같음
        score -=    # score - 1 과 같음 (*=, /= 도 같음)
    ```

14. F-String : 문자열 + 데이터유형 혼합 가능
    ```python
        f"your score is"    # 문자열 앞에 f 붙여 사용
    ```

    1) 변수 사용시 중괄호 안에 입력

    ```python
        score = 0
        
        print(f"your score is {score}")    # your score is 0 출력
    ```

<br>
<br>

## (Thonny 디버깅툴)

1. https://thonny.org/ 에서 운영체제에 맞는 버전 설치
2. 보기 > 변수 체크, 코드 작성 후 Ctrl + F5 키로 디버그 모드로 실행
3. F7 키로 하나씩 실행