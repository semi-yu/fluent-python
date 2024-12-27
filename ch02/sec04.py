"""
    Tuple
        - 명확성: 길이가 바뀌지 않을 리스트
        - 최적화: 메모리를 적게 소비함
            - 튜플 리터럴은 튜플 상수에 대한 바이트코드를 생성
            - 리스트 리터럴은 각 항목을 별도의 상수로 만들어 스택에 쌓은 후 리스트를 생성 
"""
a = (10, 'alpha', [1,2])
b = (10, 'alpha', [1,2])

print(a==b)

b[-1].append(3)
print(a==b)

"""
    - 불가변 객체만 해시가능하다. 가변 항목이 있는 튜플의 경우에는 버그의 가능성이 있다.
"""

def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    
    return True

tf = (10, 'alpha', (1, 2))
tm = (10, 'alpha', [1, 2])
print(fixed(tf), fixed(tm))