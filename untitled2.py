p=int(input("幾人?"))
r=0
score=[]
s=0
h=0
l=100
t=0
while r!=p:
    s=int(input("成績?"))
    score.append(s)
    r+=1
    t+=s
    if s>h:
        h=s
    elif s<l:
        l=s
print(score)
print("平均",t/p,"分")
print("最高",h,"分")
print("最低",l,"分")