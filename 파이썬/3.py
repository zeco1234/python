a = float(input('정수를 입력하시오:'))  #문제 3번
b = float(input('정수를 입력하시오:'))  

div, mod = divmod(a,b)

print("몫 = {}, 나머지 = {}".format(div, mod))