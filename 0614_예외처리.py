'''try:
    print("나누기 전용 계산기입니다")
    nums= []
    nums.append(int(input("첫 번째 숫자를 입력하세요.")))
    nums.append(int(input("두 번째 숫자를 입력하세요.")))
    #nums.append(int(nums[0]/nums[1]))

    print("{0} / {1} = {2}".format(nums[0],nums[1],int(nums[2])))
except ValueError:
    print("에러")
except ZeroDivisionError as err:
    print(err)
except:
    print("알 수 없는 에러가 발생")
'''
'''
try:
    print("한자리용 계산기")
    num1 = int(input("첫 번째 숫자를 입력하세요."))
    num2 = int(input("두 번째 숫자를 입력하세요."))
    if num1 >=10 or num2 >=10:
        raise ValueError
    print("{0} / {1} = {2}".format(num1,num2,int(num1/num2)))
except ValueError:
    print( " 한자리수 만 입력하시오")
'''
class BigNumberError(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg

try:
    print("한자리용 계산기")
    num1 = int(input("첫 번째 숫자를 입력하세요."))
    num2 = int(input("두 번째 숫자를 입력하세요."))
    if num1 >=10 or num2 >=10:
        raise BigNumberError("입력값 : {0} , {1}".format(num1,num2))
    print("{0} / {1} = {2}".format(num1,num2,int(num1/num2)))
except ValueError:
    print( " 한자리수 만 입력하시오")
except BigNumberError as err:
    print("빅남바에라")
    print(err)
finally: # 에러건 정상실행이건 무족권 나옴
    print(" 끝 ")
