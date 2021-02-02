import random
i=1
number=random.randint(1,20)
while i<5:
    i+=1
    num=int(input("輸入1~20"))
    if((num>20)or(num<1)):
        print("重新輸入")
    elif(num==number):
        print("猜對")
        condition=False
    elif(num<number):
        print("太小")
    elif(num>number):
        print("太大")
    else:
        print("猜錯")
