# hello_world = "엄마가 말했다. 밥 먹었니?"
# print(hello_world)
#
# name = "홍길동"
# money = 100
# print("안녕하세요. " + name + "님 반갑습니다.")
# print("입력하신 금액은 ", money, "원 입니다.")

#데이터 출력 시, % 기호 사용하는 방법
name = "jiwoo"
print("안녕하세요. 저의 이름은 %s입니다." %name)

money = 10000
print("입력하신 금액은 %d원 입니다." %money)

a = 7
b = 3
result = a + b
print(result)

#문자열 길이 구하기
hello_world = "엄마가 말했다. 밥 먹었니?"
print(len(hello_world))


#문자열 슬라이싱
자유로운_문자열 = "집에 가고 싶습니다"
print(len(자유로운_문자열))
print(자유로운_문자열[0:2])

#문자열 치환
date = "2024.07.04"
print("바꾸기 전의 데이터 :", date)
date = date.replace(".", "-")
print("바꾼 후의 데이터: ", date)

#연습문제6
var = 'abcd'
var = var.replace("a", "A")
print(var)

#연습문제5
# 1. 주어진 변수 및 데이터를 할당
old = "Python"
print(len(old))
#슬라이싱 해보기
print(old[4])
new = old[5] + old[4] + old[3] + old[2] + old[1] + old[0]
print(new)

#문자열 여러 줄 출력하기
자유로운_문자열 = ("감기에 걸려서 머리도 아프고 코도 아프고 목도 아프고 그냥 집에 가고 싶어요. \n아 머리아파 약 먹어야 하는데 귀찮아요")
print(자유로운_문자열)

