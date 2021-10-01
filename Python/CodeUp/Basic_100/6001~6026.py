# 21.10.01. 풀이

# -------------- 출력 --------------

# 6001. 출력하기01
# print( )를 이용해 다음 단어를 출력하시오.
# Hello

print("Hello")



# 6002. 출력하기02
# 공백( )을 포함한 문장을 출력하시오.
# Hello World

print("Hello World")



# 6003. 출력하기03
# 줄을 바꿔 출력하시오.
'''
Hello
World
(두 줄에 걸쳐 줄을 바꿔 출력)
'''

print("Hello")
print("World")

# 추가 참고 답안)
print("Hello\nWorld")



# 6004. 출력하기04
# 작은 따옴표(')(single quotation mark)가 들어있는 문장을 출력하시오.
# 'Hello'

print("'Hello'")



# 6005. 출력하기05
# 큰따옴표(")(double quotation mark)가 포함된 문장을 출력하시오.
# "Hello World" (단, 큰따옴표도 함께 출력한다.)

print('"Hello World"')

# 추가 참고 답안)
print("\"Hello World\"")



# 6006. 출력하기06
# 특수문자 출력하시오. 
# "!@#$%^&*()'  (단, 큰따옴표와 작은따옴표도 함께 출력한다.)

print("\"!@#$%^&*()\'")

# 추가 참고 답안)
print('"!@#$%^&*()\'')



# 6007. 출력하기07
# 윈도우 운영체제의 파일 경로를 출력하시오. 파일 경로에는 특수문자들이 포함된다.
# "C:\Download\'hello'.py" (단, 따옴표도 함께 출력한다.)

print("\"C:\Download\\'hello\'.py\"")



# 6008. 출력하기08
# 출력문 연습의 마지막 문제 - 다음과 같은 python프로그램의 소스코드를 출력하시오.
# print("Hello\nWorld") _코드를 정확히 그대로 출력하시오.(공백문자 주의)

print("print(\"Hello\\nWorld\")")


# -------------- 입출력 --------------

# 6009. 문자 1개 입력받아 그대로 출력하기
# 변수에 문자 1개를 저장한 후, 변수에 저장되어 있는 문자를 그대로 출력해보자.

a = input()
print(a)



# 6010. 정수 1개 입력받아 int로 변환하여 출력하기
# 변수에 정수값을 저장한 후 정수로 변환하여 출력해보자.

n = input()
n = int(n)
print(n)



# 6011. 실수 1개 입력받아 변환하여 출력하기
# 변수에 실수값을 저장한 후, 변수에 저장되어 있는 값을 그대로 출력해보자.

f = input()
f = float(f)
print(f)



# 6012. 정수 2개 입력받아 그대로 출력하기1
# 줄을 바꿔 정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.

a = input()
b = input()
print(a)
print(b)



# 6013. 문자 2개 입력받아 순서 바꿔 출력하기1
# 줄을 바꿔 문자(character) 2개를 입력받고, 순서를 바꿔 한 줄씩 출력해보자.

a = input()
b = input()
print(b)
print(a)



# 6014. 실수 1개 입력받아 3번 출력하기
# 실수(real number) 1개를 입력받아 줄을 바꿔 3번 출력해보자.

f = float(input())
print(f)
print(f)
print(f)


# 6015. 정수 2개 입력받아 그대로 출력하기2
# 공백을 두고 입력된정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.

a,b = input().split()
print(a)
print(b)



# 6016. 문자 2개 입력받아 순서 바꿔 출력하기2
# 공백을 두고 문자(character) 2개를 입력받아 순서를 바꿔 출력해보자.

a, b = input().split()
print(b)
print(a)



# 6017. 문장 1개 입력받아 3번 출력하기
# 정수(integer), 실수, 문자(character), 문자열(string) 등 1개만 입력받아 한 줄로 3번 출력해보자.

s = input()
print(s,s,s)



# 6018. 시간 입력받아 그대로 출력하기
# 24시간 시:분 형식으로 시간이 입력될 때, 그대로 출력하는 연습을 해보자.

a, b = input().split(':')
print(a,b,sep=':')



# 6019. 연월일 입력받아 순서 바꿔 출력하기
# "연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.

y,m,d = input().split('.')
print(d,m,y,sep='-')



# 6020. 주민번호 입력받아 형태 바꿔 출력하기
# 주민번호는 다음과 같이 구성된다. XXXXXX-XXXXXXX
# 왼쪽 6자리는 생년월일(YYMMDD)이고, 오른쪽 7자리는 성별,출생지역,확인코드로 구성되어있다.
# 주민번호를 입력받아 형태를 바꿔 출력해보자.

a, b = input().split('-')
print(a, b, sep='')



# 6021. 단어 1개 입력받아 나누어 출력하기
# 알파벳과 숫자로 이루어진 단어 1개가 입력된다.
# 입력받은 단어의 각 문자를 한 줄에 한 문자씩 분리해 출력한다.

s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])



# 6022. 연월일 입력받아 나누어 출력하기
# 6자리의 연월일(YYMMDD)을 입력받아 나누어 출력해보자.

s = input()
print(s[0:2])
print(s[2:4])
print(s[4:6])

# 추가 참고 답안)
s = input()
print(s[0:2], s[2:4], s[4:6], sep=' ')



# 6023. 시분초 입력받아 분만 출력하기
# 시:분:초 형식으로 시간이 입력될 때 분만 출력해보자

a, b, c = input().split(':')
# print(a, b, c, sep=':')
print(b[0:2], sep=':')


# 추가 참고 답안)
h, m, s = input().split(':')
print(m)



# 6024. 단어 2개 입력받아 이어 붙이기
# 알파벳 문자와 숫자로 이루어진 단어 2개를 입력받아 순서대로 붙여 출력하는 프로그램을 작성해보자.

w1, w2 = input().split()
s = w1 + w2
print(s)

# 추가 참고 답안)
a, b = input().split()
print(a+b)



# -------------- 값변환 --------------

# 6025. 정수 2개 입력받아 합 계산하기
# 정수 2개를 입력받아 합을 출력하는 프로그램을 작성해보자.

a, b = input().split()
c = int(a) + int(b)
print(c)

# 추가 참고 답안)
a, b = input().split()
a=int(a)
b=int(b)
c=a+b
print(c)



# 6025. 실수 2개 입력받아 합 계산하기
# 실수 2개를 입력받아 합을 출력하는 프로그램을 작성해보자.

a = float(input())
b = float(input())
print(a + b)

# 추가 참고 답안)
a=input()
b=input()
a=float(a)
b=float(b)
c=a+b
print(c)
