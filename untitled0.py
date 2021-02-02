m=input("數學分數?")
m=int(m)
e=input("英文分數?")
e=int(e)
if not(m>=0 and m<=100):
    print("重新輸入")
if(e<0 and e>100):
    print("重新輸入")
elif(m>=90 and e>=90)or(m==100)or(e==100):
     print("有獎")
else:
     print("沒獎")