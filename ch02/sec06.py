"""
    시퀀스 패턴 매칭
"""
from collections import namedtuple

def handle(message):
    Info = namedtuple('Info', ['nationality', 'name', 'age'])

    match message:
        # 첫 항목은 'NAT' 이어야 한다. 그 다음은 변수가 하나 있다.
        case ('NAT', nationality):
            Info.nationality = nationality
        case ('NAM', name):
            Info.name = name
        case ('AGE', age):
            Info.age = age
        # 타입으로 매칭한다.
        case (str(id), str(nationality), str(name), int(age)):
            Info.id = id
            ...
        case _:
            raise Exception()

# 코드 파싱도 가능하겠다.

def parse(expression):
    match expression:
        case ('def', function_name, '(', *parameter, '):'):
            print(f'function name {function_name}, function parameter {parameter}')
        case _:
            raise Exception('wrongful format')
        

parse(('def', 'foo', '(', 'name', 'age', 'nationality','):'))
parse(('def', 'bar', '(', '):'))
parse(('fn', 'baz', '(', ')'))