"""
    시퀀스, 반복형 객체 언패킹
"""

# 병럴 할당
lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates

print(latitude, longitude)

expr = (36, 9)
quotient, remainder = divmod(*expr)
print(quotient, remainder)