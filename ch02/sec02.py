"""
    Sequence
"""
import array

from memory_profiler import profile

"""
    컨테이너 시퀀스
        - 다른 자료형 항목을 하나의 시퀀스 안에 수용
        - 참조를 가르킴
"""
container_seq = ['cat', 100, 12.9, []]

"""
    균일 시퀀스
        - 동일 자료형만 하나의 시퀀스 안에 수용
        - 값을 직접
            - 기본 자료형만 가능
"""
flat_seq = array.array('d', [13.4, 67.0])


"""
    지능형 리스트 list comp

    - 리스트를 실제로 생성함
"""
colors = ['black', 'white']
sizes = ['XS', 'S', 'M', 'L', 'XL']


# streching variable scope with walrus

symbol = 'abcdefg'

code = [last := ord(s) for s in symbol]

@profile
def make_list_comp():
    shirts = [(color, size) for color in colors
                            for size in sizes]
    
    for c, s in shirts: print(f'{c} {s}') 

    return shirts
make_list_comp()

# print(s) it will raise an error
print(last)

"""
    제너레이터 표현식 genexpr
    - 
"""

@profile
def make_genexpr():
    shirts = ((color, size) for color in colors
                            for size in sizes)
    
    for c, s in shirts: print(f'{c} {s}')
make_genexpr()
