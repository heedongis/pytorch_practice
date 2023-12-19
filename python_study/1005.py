# 일반적 변수 선언 후 평균값 구하기
# korean = 80
# english = 75
# math = 55
#
# average = (korean + english + math)/3
# print('평균 :',average)

'''
    홍길동
    국어 : 80
    영어 : 75
    수학 : 55
'''

hong_subject = ['국어', '영어', '수학']
hong_score = [80, 75, 55]  # [국어, 영어, 수학]
#
# total = hong[0] + hong[1] + hong[2]
# average = total / len(hong)
#
# print()

# total = 0
# for score in hong_score:
#     total = total + score
#
# average = total / len(hong_score)
#
# print(average)

# num = 13
# mod = num % 2 # 1이면 홀수 0이면 짝수
#
# if mod == 1:
#     print('홀수')
# else:
#     print('짝수')
#

# 주민번호 뒷자리 첫번째가 1이면 남자 2면 여자

# pin = "891224-2036511"
# yyyymmdd = "19"+pin[0:6]
# # print(yyyymmdd)
# gender = pin[7]
#
# if gender == '1':
#     print('남자')
# elif gender == '2':
#     print('여자')


# a = "a:b:c:d"
# b = a.replace(':', '#')
# print(b)

# a = [1,3,5,4,2]
# a.sort(reverse=True)
# print(a)
# a.
# print()
#
# money = True
#
# if money:
#     print('머니')
#     print('money')
#
#     print('머니머니')

# a = b
# a >= b
# b <= a

# x = 3
# y = 2
#
# judge = x < y # 참 True
# print(judge)
#
# judge = 4 not in [1,2,3]

# pocket = ['card', 'money', 'coin']
#
# if 'money' in pocket:
#     pass
# else:
#     print('걸어가라')
#
# score = 50
# message = "success" if score >= 60 else "fail"
#
# print(message)

treeHit = 0
while treeHit < 10:
    if treeHit == 10:
        print("나무가 넘어갑니다.")
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)



