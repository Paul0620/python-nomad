# Python

1. [파이썬이란](#파이썬이란)
2. [사용범위](#사용범위)
3. [특징](#특징)
4. [장점](#장점)
5. [수업내용](#수업내용)
   - [1일차 - 변수, 리스트, 튜플, 딕셔너리, 함수(print)](#1일차)
   - [2일차](#2일차)
   - [3일차](#3일차)
   - [4일차](#4일차)
   - [5일차](#5일차)
   - [6일차](#6일차)
   - [7일차](#7일차)
   - [8일차](#8일차)
   - [9일차](#9일차)
6. [과제](#과제)

<br><br>

## 파이썬이란

- 파이썬은 1991년 귀도 반 로섬(Guido van Rossum)이라는 프로그래머에 의해 개발된 언어로, 가독성이 높고 쉬운 문법 덕택에 다른 프로그래밍 언어보다 빠른 습득이 가능하다는 특징이 있다. 그 덕에 프로그래밍을 전공하지 않은 비전공자 중심으로 인기를 얻어 데이터 분석과 모델링을 다루는 통계학부터 딥러닝과 인공지능을 활용하는 의학에까지 다양한 분야에 두루 활용되고 있다.

<br>

## 사용범위

- 시스템 유틸리티 제작 - 파이썬은 운영체제의 시스템 명령어를 사용할 수 있는 각종 도구를 갖추고 있기 때문에 이를 바탕으로 갖가지 시스템 유틸리티(컴퓨터 사용에 도움을 주는 여러 소프트웨어)를 만드는데 유리.

- GUI프로그래밍 - GUI(Graphic User Interface) 프로그래밍이란 화면에 또 다른 윈도우 창을 만들고 그 창에 프로그램을 동작시킬 수 있는 메뉴나 버튼, 그림 등을 추가. 파이썬은 GUI 프로그래밍을 위한 도구가 잘 갖추어져 있어 만들기 쉬움. ex) Tkinter(파이썬 GUI Toolkit)를 사용.

- C/C++와의 결합 - 파이썬은 접착(glue) 언어라도고 부르는데, 다른 언어와 잘 어울려 결합해서 사용할 수 있기 때문. C나 C++로 만든 프로그램을 파이썬에서 사용 가능 그 반대의 경우도 가능하다.

- 데이터베이스 프로그래밍 - 파이썬은 사이베이스(Sybase), 인포믹스(Infomix), 오라클(Oracle), 마이에스큐엘(MySQL), 포스트그레스큐엘(PostgreSql) 등의 데이터 베이스에 접근하기 위한 도구를 제공한다. 이 이외에 피클(Pickle)이라는 모듈을 사용할 수도있음.

- 데이터 분석, 사물 인터넷 - 파이썬으로 만든 판다스(Pandas) 모듈을 사용하면 데이터 분석을 더 쉽고 효과적으로 할 수 있음. 사물 인터넷 분야에서는 라즈베리파이(Raspberry Pi)라는 리눅스 기반의 아주 작은 컴퓨터가 있는데 이 컴퓨터는 홈시어터나 작은 게임기 등 에 사용된다. 이 컴퓨터를 제어하는 용으로 파이썬을 사용한다.

<br>

## 특징

- 스크립트 언어(Script language) - 컴파일 과정 업이 인터프리터(Interpreter, 해석기)가 소스 코드를 한 줄씩 읽어들여 곧바로 실행하는 스크립트 언어. 때문에 컴파일 과정이 필요하지 않아 실행결과를 바로 확인하고 수정하면서 손쉽게 코드를 작성 할 수 있다.

  - 컴파일 언어와 스크립트 언어의 차이점은? - 컴파일 언어는 '컴파일' 과정을 통해 프로그래머(인간)이 작성한 코드를 기계어로 번역해 실행하는 언어이다. 컴파일 언어는 소스 코드를 컴파일하는 과정을 거쳐야 하므로 실행 및 수정에 비교적 많은 시간을 소요하지만, 한번 기게어로 번역되면 빠른 실행 속도를 보여준다. <br>
    스크립트 언어는 컴파일 없이 곧바로 실행하므로 결과를 바로 확인하고 빠르게 수정할 수 있지만, 번역과 실행이 돌시에 이루어져 컴파일 언어보다 느린 실행속도를 보임.

- 동적 타이핑(Dynamic typing) - 파이썬은 동적 타입의 언어이다. 변수의 자료형을 지정하지 않고 단순히 선언하는 것만으로도 값을 지정할 수 있다. 이때 자료형은 코드가 실행되는 시점에 결정된다. 또한 변환시에도 번거로운 과정을 거치지 않아도 된다는 장점이 있지만, 코드 실행 도중 예상하지 못한 타입으로 인한 에러가 발생할 수 있는 점이 있다.

- 플랫폼 독립적(Platform-independent) - 파이썬은 리눅스(Linux), 유닉스(Unix), 윈도우즈(Windows), 맥(Mac) 등 대부분의 운영체제(Operating System, OS)에서 모두 동작한다. 운영체제별로 컴파일할 필요가 없기 때문에 한 번 소스 코드를 작성하면 어떤 운영체제에서든 활용이 가능

<br>

## 장점

- 간결하고 쉬운 문법 - 파이썬은 인간의 사고와 유사한 문법을 지니고 있다. 때문에 많은 시간을 들이지 않고도 파이썬 문법을 학습할 수 있고, 프로그래밍을 전공으로 하지 않은 사람도 수일 내에 파이썬을 익혀 활용하는 것이 가능하다.

- 빠른 개발 속도 - 쉽고 간결한 문법 덕에 높은 생산성을 자랑한다. 파이썬을 활용할 경우 더 적은 코드로 더 많은 작업을 수행할 수 있으며, 복잡한 구문으로 인한 오류 발생을 줄여 그 어떤 프로그래밍 언어보다 빠른 개발이 가능하다.

- 높은 확장성 및 이식성 - 파이썬은 대표적인 글루(Glue) 언어에 해당한다. 다른 언어나 라이브러리에 쉽게 접근해 연동할 수 있기 때문이다. 높은 성능의 애플리케이션 개발이 필요한 경우 C/C++과 같은 언어를 파이썬과 결합해 사용할 수 있다.

- 활발한 생태계 - 파이썬은 수 많은 표준 라이브러리를 제공한다. 그 덕에 프로그래머는 모든 코드를 일일이 작성할 필요가 없다. 그리고 폭넓은 생태계와 활발한 커뮤니티 활동으로 인해 빠르게 문제를 해결하고, 협업할 수 있다. 대표적으로 [PyPi](https://pypi.org/)와 같은 웹사이트를 통해 작성한 파이썬 패키지를 공유하고 다른 개발자가 배포한 패키지를 pip 명령어를 통해 간단하게 설치할 수 있다.

<br>

## 수업내용

### 1일차

### 변수, 리스트, 튜플, 딕셔너리, 함수

### 1. 변수

- 변수란? - 어떠한 것을 담아 놓는 상자
- 변수는 정수, 실수, 문자, 문자열, 참/거짓(boolean)을 담을 수 있음

```py
a_string = "like this" #문자열
a_number = 3 #정수
a_float = 3.12 #실수
a_boolean = False #참/거짓
a_none = None #파이썬에만 있음(존재하지 않음을 뜻하는 의미) == null

#변수의 타입을 보는방법
type(변수명)
```

### 2. 리스트(list)

- 열거형 타입(Sequence Type)

```py
days = ["Mon", "Tue", "Wed", "Thur", "Fri"]
#리스트의 순서는 0부터 시작하기 때문에 3번째 "Web"를 출력하고 싶다면 [2]로
days[2]
#len 리스트의 길이(갯수)
len(days)
#append 변수하나를 리스트에 추가 가장 뒷부분에 추가됨
days.append("Sat")
#insert(index값, 넣을 값)
days.insert(0, "Sat")
#del 리스트명[해당값] - 키워드를 통한 삭제
del days["Wed"]
#remove(해당값) - remove메소드에 의한 삭제
days("Wed")
#순서 뒤집기
days.reverse()
#순서 정렬
days.sort()
```

### 3. 튜플(tuple)

- 아무도 변경할 수 없는 리스트를 만들고 싶을때 ()로 감싸서 만듬

```py
days = ("Mon", "Tue", "Wed", "Thur", "Fri")
#값을 추가, 삭제, 변경이 불가
```

### 4. 딕셔너리(dict)

- {}안에 이름 그대로 사전형태로 저장한다. Key-Value가 한쌍이며 여러개를 담을때 쉼표(,)로 구분하여 넣는다
- 리스트, 튜플처럼 순차적으로 해당 값을 구하지 않고 Key를 통해 Value를 얻는다.
- 키값의 이름이 같으면 안된다.(키명은 고유한 명칭)

```py
#Dicts 사전 - {}로 감싼다
nico = {
  "name" : "Nico",
  "age" : 29,
  "korean" : True,
  "fav_food" : ["Kimchi", "Sashimi"] #딕셔너리안에 배열로 담을수도 있음
}
#Key값 name의 Value값 출력
print(nico["name"])
#딕셔너리 nico를 출력
print(nico)
#사전에 데이터 추가 - 딕셔너리명[Key값] = 넣을 값
nico["handsome"] = True
#삭제하기 - del 딕셔너리명[Key값]
del nico["name"]
```

### 5. 함수(Function) print

- 어떠한 기능을 여러번 사용할 수 있도록 만든 것

```py
age = "18"
print(type(age))
#str로 입력한 18을 숫자 18로 변환
n_age = int(age)
print(type(n_age))

def say_hello():
  print("hello")
  print("bye")

say_hello()
```
