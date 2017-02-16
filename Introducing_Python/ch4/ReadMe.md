# Chapter 4

### 여러 시퀀스 순회하기: `zip()`
`zip()` 함수를 사용하면 여러 시퀀스를 병렬로 순회할 수 있다.

```python
days = ['Monday', 'Tuesday', 'Wednseday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']

for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
	print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)
```

여러 시퀀스 중 가장 짧은 시퀀스가 완료되면 `zip()`은 멈춘다.  
`zip()`함수로 여러 시퀀스를 순회하며, 동일한 오프셋에 있는 항목으로부터 튜플을 만들 수 있다. `zip()`에 의해 반환되는 값은 튜플이나 리스트 자신이 아니라 하나로 반환될 수 있는 순회 가능한 값이다.

### 숫자 시퀀스 생성하기: `range()`
`range()`함수는 리스트나 튜플 같은 자료구조를 생성하여 저장하지 않더라도 특정 범위 내에서 숫자 스트림을 반환한다. 이것은 컴퓨터 메모리를 전부사용하지 않고, 프로그램의 충돌없이 아주 큰 범위를 생성할 수 있게 해준다. `range()` 함수는 슬라이스의 사용법과 비슷하다. `range(start, stop, step)` 형식을 사용한다.

## 컴프리헨션
컴프리헨션은 하나 이상의 이터레이터로부터 파이썬의 자료구조를 만드는 콤팩트한 방법이다. 컴프리헨션은 비교적 간편한 구문으로 반복문과 조건 테스트를 결합할 수 있도록 해준다.

### 리스트 컴프리헨션
```python
number_list = list(range(1, 6))
```
위의 방법보다 리스트 컴프리헨션을 사용해서 리스트를 만드는 것이 조금 더 파이써닉한 방법이다.  
[표현식 `for` 항목 `in` 순회 가능한 객체]

```python
number_list = [number for number in range(1, 6)]
number_list = [number-1 for number in range(1, 6)]
a_list = [number for number in range(1, 6) if number % 2 == 1]
[1, 3, 5]
```
루프가 중첩될 수 있는 것처럼, 컴프리헨션에서 루프에 상응하는 하나 이상의 `for ...`절을 사용할 수 있다. 

```python
rows = range(1,4)
cols = range(1,3)
for row in rows:
	for col in cols:
		print(row, col)
```
이제 컴프리헨션을 사용해보자. `(row, col)` 튜플 리스트를 만들어서 `cells` 변수에 할당한다.

```python
cells = [(row, col) for row in range(1,4) for col in range(1,3)]
for cell in cells:
	print(cell)
```

### 딕셔너리 컴프리헨션
리스트 못지않게 딕셔너리 또한 컴프리헨션이 있다.  
{키_표현식 : 값_표현식 `for` 표현식 `in` 순회 가능한 객체}

리스트 컴프리헨션과 같이 딕셔너리 컴프리헨션 또한 `if` 테스트와 다중 `for ...`절을 가질 수 있다.

### 셋 컴프리헨션
{표현식 `for` 표현식 `in` 순회 가능한 객체}

### 제너레이터 컴프리헨션
튜플은 컴프리헨션이 없다. `()`안에 리스트와 동일한 컴프리헨션을 작성했을시 제너레이터 객체를 반환한다. 제너레이터는 이터레이터에 데이터를 제공하는 하나의 방법이다.

> 제너레이터는 한 번만 실행될 수 있다. 리스트, 셋, 문자열, 딕셔너리는 메모리에 존재하지만, 제너레이터는 즉석에서 그 값을 생성하고, 이터레이터를 통해서 한 번에 값을 하나씩 처리한다. 제너레이터는 이 값을 기억하지 않으므로 다시 시작하거나 제너레이터를 백업할 수 없다.

## 함수
함수롤 전달한 값을 argument라고 부른다. argument와 함수를 호출하면 argument의 값은 함수 내에서 해당하는 parameter에 복사된다. 위치 argument와 키워드 argument를 섞어서 쓸 수 있다. 다만 위치 argument가 먼저 와야 한다.

### 기본 parameter값 지정하기
parameter에 기본값을 지정할 수 있다. argument를 제공하지 않으면 기본값을 사용한다.

> 기본 argument값은 함수가 실행될 때 계산되지 않고, 함수를 **정의**할 때 계산된다. 파이썬을 막 시작한 프로그래머는 리스트 혹은 딕셔너리와 같은 변경 가능한 데이터 타입을 기본 argument로 사용할 때 실수를 하게 된다.

### 위치 argument 모으기: `*`
함수의 parameter에 애스터리스크를 사용할 때, 애스터리스크는 parameter에서 위치 argument 변수들을 튜플로 묶는다. `print_args()` 함수에 argument를 전달하여, `args` parameter의 튜플 결과를 살펴보자

```python
def print_args(*args):
	print('Positional argument tuple:', args)
```
함수를 argument 없이 호출하면 `*args`에는 아무것도 없다.

```python
print_args()
Positional argument tuple: ()
```
argument를 넣어서 `args` 튜플을 출력해보자

```python
print_args(3, 2, 1, 'wait!', 'uh...')
Positional argument tuple: (3, 2, 1, 'wait!, 'uh...')
```
가변 argument를 사용하는 `print()`와 같은 함수는 매우 유용하다. 함수에 위치 argument를 지정할 때 맨 끝에 `*args`를 써서 나머지 인자를 모두 취하게 할 수 있다.

```python
def print_more(required1, required2, *args):
	print('Need this one:', required1)
	print('Need this one too:', required2)
	print('All the rest:', args)
	
print_more('cap, 'gloves', 'scarf', 'monocle', 'mustache wax')
Need this one: cap
Need this one too: gloves
All the rest: ('scarf', 'monocle', 'mustache wax')
```

`*`를 사용할 때 가변 argument의 이름으로 `args`를 사용할 필요가 없지만 관용적으로 `args`를 사용한다.

### 키워드 argument 모으기: `**`
키워드 argument를 딕셔너리로 묶기 위해 두 개의 애스터리스크(`**`)를 사용할 수 있다. argumnet의 이름은 키고, 값은 이 키에 대응하는 딕셔너리 값이다. 다음 예제는 `print_kwargs()` 함수를 정의하여 키워드 argument를 출력한다.

```python
def print_kwargs(**kwargs):
	print('Keyword arguments:', kwargs)
```
키워드 argument를 넣어서 함수를 호출해보자.

```python 
print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')
Keyword arguments: {'dessert': 'macaroon', 'entree': 'mutton', 'wine': 'merlot'}
```
함수 안에 `kwargs` 딕셔너리가 있다.  
위치 parameter `*args`, `**kwargs`를 섞어서 사용하려면 이들을 순서대로 배치해야 한다. 그리고 `args`와 마찬가지로 키워드 pararmeter의 이름을 `kwargs`로 할 필요는 없지만 관용적으로 `kwargs`를 사용한다.

### 일등 시민: 함수
'모든 것이 객체다' 라는 파이썬의 철학은 파이썬의 만트라이기도 하다. 객체는 숫자, 문자열, 튜플, 리스트, 딕셔너리, 그리고 함수를 포함한다. 파이썬에서 함수는 일등 시민이다.

```python
def run_something_with_args(func, arg1, arg2):
	func(arg1, arg2)
```
이것을 `*args`, `**kwargs` argument와 결합해서 사용할 수 있다.  
여러 개의 위치 argument를 취하는 함수를 정의해보자. `sum()` 함수를 사용해서 이 argument들을 더한 값을 반환한다.

```python
def sum_args(*args):
	return sum(args)
```
`sum()`함수는 순회 가능한 숫자(정수 혹은 부동소수점수) 인자의 값을 모두 더하는 파이썬 내장 함수다.  
함수와 여러 개의 위치 argument를 취하는 새로운 `run_with_positional_args()` 함수를 정의한다.

```python
def run_with_positional_args(func, *args):
	return func(args)
```
이 함수를 다음과 같이 호출해보자.

```python
run_with_positional_args(sum_args, 1, 2, 3, 4)
10
```
함수를 리스트, 튜플, 셋, 딕셔너리의 요소로 사용할 수 있다. 함수는 불변하기 때문에 딕셔너리의 키로도 사용할 수 있다.

### 클로져
내부 함수는 **클로져(closure)**처럼 행동할 수 있다. 클로져는 다른 함수에 의해 동적으로 생성된다. 그리고 바깥 함수로부터 생성된 변수값을 변경하고, 저장할 수 있는 함수다.

* `inner2()`는 인자를 취하지 않고, 외부 함수의 변수를 직접 사용한다.
* `knights2()`는 `inner2` 함수 이름을 호출하지 않고, 이를 반환 한다.

```python
def knights2(saying):
	def inner2():
		return "We are the knights who say: '%s'" % saying
	return inner2
```
`inner2()`함수는 `knights2()` 함수가 전달받은 `saying` 변수를 알고 있다. 코드에서 `return inner2`라인은 (호출되지 않은) `inner2`함수의 특별한 복사본을 반환한다. 이것이 외부 함수에 의해 동적으로 생성되고, 그 함수의 변수값을 알고 있는 함수인 클로져다.  
다른 인자를 넣어서 `knights2()` 함수를 두번 호출해보자.

```python
a = knights2('Duck')
b = knights2('Hasenpfeffer')
```
`a`와 `b`의 타입은 무엇일까?

```python
type(a)
<class 'function'>
type(b)
<class 'fucntion'>
```
이들은 함수이지만, 클로져이기도 하다.

```python
a 
<function knights2.<locals>.inner2 at 0x01>
b
<function knights2.<locals>.inner2 at 0x11>
```
이들을 호출하면, `knights2()` 함수에 전달되어 사용된 `saying`을 기억한다.

```python
a()
"We are the knights who say: 'Duck'"
b()
"We are the knights who say: 'Hasenpfeffer'"
```

### 익명 함수: `lambda()`
파이썬의 람다 함수는 단일문으로 표현되는 익명 함수다. `edit_story()`함수를 정의해보자. argument는 다음과 같다.

* `words`: `word` 리스트
* `func`: `words`의 각 `word` 문자열에 적용되는 함수

```python
def edit_story(words, func):
	for word in words:
		print(func(word))
```
이제 `words` 리스트와 각 `word`에 적용될 함수가 필요하다. 

```python
stairs = ['thud', 'meow', 'thud', 'hiss']
edit_story(stairs, lambda word: word.capitalize() + '!')
Thud!
Meow! 
Thud!
Hiss!
```
람다에서 하나의 `word` argument를 취했다. 람다은 콜론(`:`)과 닫는 괄호 사이에 있는 것이 함수의 정의 부분이다. 람다는 많은 작은 함수를 정의하고, 이들을 호출해서 얻은 모든 결과값을 저장해야 하는 경우에 유용하다. 

## 제너레이터
제너레이터는 파이썬의 시퀀스를 생성하는 객체다. 제너레이터로, 전체 시퀀스를 한 번에 메모리에 생성하고 정렬할 필요 없이, 잠재적으로 아주 큰 시퀀스를 순회할 수 있다. 제너레이터는 이터레이터에 대한 데이터의 소스로 자주 사용된다. `range()`도 제너레이터이다. 제너레이터를 순회할 때마다 마지막으로 호출된 항목을 기억하고 다음 값을 반환한다. 제너레이터는 일반 함수와 다르다. 일반 함수는 이전 호출에 대한 메모리가 없고, 항상 똑같은 상태로 첫 번째 라인부터 수행한다.  
잠재적으로 큰 시퀀스를 생성하고, 제너레이터 컴프리헨션에 대한 코드가 아주 긴 경우에는 **제너레이터 함수**를 사용하면 된다. 이것은 일반 함수지만 `return`문으로 값을 반환하지 않고, `yield`문으로 값을 반환한다.

```python
def my_range(first=0, last=10, step=1):
	number = first
	while number < last:
		yield number 
		number += step
```
다음과 같이 제너레이터 객체를 반환한다.

```python
ranger = my_range(1, 5)
for x in ranger:
	print(x)	
1
2
3
4
```

## 데커레이터
가끔씩 소스 코드를 바꾸지 않고, 사용하고 있는 함수를 수정하고 싶을 때가 있다. 일반적인 예는 함수에 전달된 인자를 보기 위해 디버깅 문을 추가하는 것이다. **데커레이터(decorator)**는 하나의 함수를 취해서 또 다른 함수를 반환하는 함수다. 이 파이썬 묘책을 사용하기 위해서는 다음과 같은 무기를 사용한다.

* `*args`와 `**kwargs`
* 내부 함수
* 함수 argument

`document_it()`함수는 다음과 같이 데커레이터를 정의한다.

* 함수 이름과 argument값을 출력한다.
* argument로 함수를 실행한다.
* 결과를 출력한다.
* 수정된 함수를 사용할 수 있도록 반환한다.

코드는 다음과 같다.

```python
def document_it(func):
	def new_function(*args, **kwargs):
		print('Running function:', func.__name__)
		print('Positional arguments:', args)
		print('Keyword arguments:', kwargs)
		result = func(*args, **kwargs)
		print('Result:', result)
		return result
	return new_function
```
`document_it()`함수에 어떤 `func` 함수 이름을 전달하든지 간에 `document_it()`함수에 추가 선언문이 포함된 새 함수를 얻는다. 데커레이터는 실제로 `func` 함수로부터 코드를 실행하지 않는다. 하지만 `document_it()`함수로부터 `func`를 호출하여 결과뿐만 아니라 새로운 함수를 얻는다.  
그러면 데커레이터를 어떻게 사용할까? 수동으로 데커레이터를 적용해보자.

```python
def add_ints(a, b):
	return a + b

cooler_add_ints = document_it(add_ints) # 데커레이터를 수동으로 할당
cooler_add_int(3, 5)
Running function: add_ints
Positional arguments: (3, 5)
Keyword arguments: {}
Result: 8
8
```
위와 같이 수동으로 데커레이터를 할당하는 대신, 다음과 같이 데커레이터를 사용하고 싶은 함수에 그냥 `@데커레이터_이름`을 추가한다.

```python
@document_it
def add_ints(a, b):
	return a + b
		
add_ints(3, 5)
Running function: add_ints
Positional arguments: (3, 5)
Keyword arguments: {}
Result: 8
8
```
함수는 여러 개의 데커레이터를 가질 수 있다. 결과를 제곱하는 `square_it()` 데커레이터를 작성해보자.

```python
def square_it(func):
	def new_function(*args, **kwargs):
		result = func(*args, **kwargs)
		return = result * result
	return new_function
```
함수에서 가장 가까운(`def`바로 위) 데커레이터를 먼저 실행한 후, 그 위의 데커레이터가 실행된다. 이 예제에서는 순서를 바꿔도 똑같은 결과를 얻지만, 중간 과정이 바뀐다.

```python
@document_it
@square_it
def add_ints(a, b):
	return a + b

add_ints(3, 5)
Running function: new_function
Positional arguments: (3, 5)
Keyword arguments: {}
Result: 64
64

@square_it
@document_it
def add_ints(a, b):
	return a + b
	
add_ints(3, 5)
Running functions: add_ints
Positional arguments: (3, 5)
Keyword arguments: {}
Result: 8
64
```

## 네임스페이스와 스코프
이름(name)은 사용되는 위치에 따라 다른 것을 참조할 수 있다. 파이썬 프로그램에서는 다양한 네임스페이스(namespace)가 있다. 네임스페이스는 특정 이름이 유일하고, 다른 네임스페이스에서의 같은 이름과 관계가 없는 것을 말한다.  
각 함수는 자신의 네임스페이스를 정의한다. 메인 프로그램에서 `x`라는 변수를 정의하고, 함수에서 `x`라는 변수를 정의했을 때, 이들은 서로 다른 것을 참조한다. 하지만 이 경계를 넘을 수 있다. 다양한 방법으로 다른 네임스페이스의 이름을 접근할 수 있다. 메인 프로그램은 전역 네임스페이스를 정의한다. 이와 같이 이 네임스페이스의 변수들은 전역 변수다. 함수로부터 전역 변수의 값을 얻을 수 있다.

```python
animal = 'fruitbat'
def print_global():
	print('inside print_golbal:', animal)
```
함수에서 전역 변수의 값을 얻어서 바꾸려 하면 에러가 발생한다.

```python
def change_and_print_global():
	print('inside change_and_print_global:', animal)
	animal = 'wombat'
	print('after the change:', animal)

change_and_print_global()
UnboundLocalError: local variable 'animal' referenced before assignment
```
지역 변수를 먼저 선언해야 한다는 에러를 얻을 수 있다.

```python
def change_local():
	animal = 'wombat'
	print('inside change_local:', animal, id(animal))
```
`change_local()`함수 또한 이름이 `animal`인 변수를 갖지만, 그것은 로컬 네임스페이스 안에 있다. 함수 내의 지역 변수가 아닌 전역 변수를 접근하기 위해 `global` 키워드를 사용해서 전역 변수의 접근을 명시해야 한다(파이썬 철학: 명확한것이 함축적인 것보다 낫다).

```python
def change_and_print_global():
	global animal
	animal = 'wombat'
	print('inside change_and_print_global:', animal)
 
animal
'fruitbat'
change_and_print_global()
inside change_ang_print_global: wombat
animal
'wombat'
```
함수 안에 `global` 키워드를 사용하지 않으면 파이썬은 로컬 네임스페이스를 사용하고 변수는 지역 변수가 된다. 지역 변수는 함수를 수행한 뒤 사라진다. 파이썬은 네임스페이스의 내용을 접근하기 위해 두 가지 함수를 제공한다.

* `locals()`함수는 로컬 네임스페이스의 내용이 담긴 딕셔너리를 반환한다.
* `globals()`함수는 글로벌 네임스페이스의 내용이 담기 딕셔너리를 반환한다.

이들을 사용해보자.

```python
animal = 'fruitbat'
def change_local():
	animal = 'wombat' # 지역 변수
	print('locals:', locals())

animal
'fruitbat'
change_local()
locals: {'animal': 'wombat'}
print('globals:', globals()) # 보여주기 위한 작은 출력 포맷
globals: {
	'__doc__': None,
	'__package__': None,
	'__loader__': <class '_frozen_importlib.BuiltinImporter'>,
	'change_local': <function change_local at 0x100516f28>,
	'__spec__': None, 
	'animal': 'fruitbat', 
	'__name__': '__main__', 
	'__builtins__': <module 'builtins' (built-in)>
}
```
`change_local()`함수 내의 로컬 네임스페이스에는 `animal` 로컬 변수만 포함되어 있다. 메인 프로그램의 글로벌 네임스페이스에는 `animal` 글로벌 변수와 다른 여러 가지 것들이 포함되어 있다.

## 이름에 `_`와 `__` 사용
두 언더스코어(`__`)로 시작하고 끝나는 이름은 파이썬 내의 사용을 위해 예약되어 있다. 그러므로 변수를 선언할 때 두 언더스코어를 사용하면 안 된다. 애플리케이션 개발자들이 이와 같은 변수 이름을 선택할 가능성이 낮아서, 이러한 네이밍 패턴을 선택한 것이다. 예를 들어 함수의 이름은 시스템 변수 `function.__name__`에 있다. 그리고 함수의 `docstring`은 `function.__doc__`에 있다. 조금 전에 `globals()` 함수 출력 결과에서 봤듯이, 메인 프로그램은 특별한 이름 `__main__`으로 할당되어 있다.

## 에러 처리하기: `try`, `except`
`try` 블록 안의 코드를 실행할 때 에러가 있다면 예외가 발생하고 `except` 블록 내의 코드가 실행된다. 만약 `try`블록 안에 에러가 없다면 `except`블록은 건너 뛴다.

```python
short_list = [1, 2, 3]
position = 5
try: 
	short_list[position]
except:
	print("Need a position between 0 and', len(short_list)-1,)
```
예외 타입을 넘어 예외사항에 대한 세부정보를 얻고 싶다면 다음과 같이 변수 이름에서 예외 객체 전체를 얻을 수 있다.  
`except` 예외 타입 `as` 이름  

