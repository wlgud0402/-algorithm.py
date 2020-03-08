#절댓값 알고리즘1 (부호판단)
a = int(input("정수입력"))
def absolute_value(abc):
    # global a
    if abc >= 0:
        print(abc)
    else:
        print(-abc)

absolute_value(a)

def abs_sign(a):
    if a >=0:
        return a
    else:
        return -a

#절댓값 알고리즘2 (제곱,제곱근)
import math  #수학 모듈을 사용해서 제곱근을 구할 수 있다

def abs_square(a):
    b = a*a
    return math.sqrt(b)   #제곱근은 소수점이 붙은 0.0값을 출력함

print(abs_sign(-3))
print(abs_square(-6))
