"""
    Imitating numericals

    원서에서는 모듈 이름을 vector2d.py로 두고있음.    
"""
import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        """
            abs() 함수에 의해 호출

            math.hypot() 함수를 사용할 수 있다.
            math.hypot(self.x, self.y)
        """
        return math.sqrt(self.x**2 + self.y**2)

    def __repr__(self):
        """
            __repr__ 메서드에 의해 반환되는 문자열은 가급적 객체 생성 코드와 일치해야 한다.

            __str__과 __repr__ 구현 중에서는 __repr__을 우선하라.
            
            둘 간의 차이는 fpy.li/1-5를 참고하라.

            - repr() 내장 메서드에 의해 호출
                - 대화형 콘솔은 repr()을 호출함
                - 디버거는 repr()을 호출함
                - %r 플레이스홀더는 repr()을 호출함
                - f-string은 repr()을 호출함
                    - 단, !r로 명기된 경우에.
                      print(f'His name is {name!r}')
        """
        return f'Vector({self.x}, {self.y})'
    
    def __add__(self, other):
        """
            + 연산자에 의해 호출
        """
        return Vector(self.x + other.y, 
                      self.y + other.y)
    
    def __mult__(self, scalar):
        """
            * 연산자에 의해 호출
        """
        return Vector(scalar * self.x,
                      scalar * self.y)
    
    def __bool__(self):
        """
            불리언 값
            bool 내장 메서드에 의해 호출

            bool() 함수는
            1. __bool__을 호출한다.
            2. __bool__이 구현되지 않으면 __len__을 호출한다.
                len 값이 0이면 거짓이다.
            3. __len__도 구현되지 않으면 무조건 참이다.
        
            책의 구현방법: bool(abs(self))
                - 길이가 0이면 거짓이다. 길이가 0이 아니면 참이다.

            더 빠르고 가독성이 안좋은 방법: bool(self.x or self.y)
            속성 x와 y에 의존하므로 제곱근 및 덧셈 연산이 필요없다.
        """
        return bool(abs(self))
    

"""
    추상베이스클래스(ABC)

      언패킹
      for
      이 외 반복          len()             in
    [ Iterable ]        [ Sized ]       [ Container ]
      __iter__           __len__         __contains__
      Δ     Δ               Δ                 Δ
      |     |               |                 |
      |     *---------------+-----------------+
      |                     |
    [ Reversible ]    [ Collection ]
      __reversed__          Δ
      Δ                     |  
      |                     |
      |                     |
      |      +--------------+--------------+
      |      |              |              |
    [ Sequence ]        [ Mapping ]     [ Set ]

     <순서있는>                 <순서없는>

    - dict는 삽입 순서만 유지하지, key의 순서를 유지하진 않는다.
"""