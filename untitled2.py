def high(scores):
    hs=100
    n=len(scores)
    for i in range(n):
        if scores[i]<=hs:
           scores[i]=hs
           hname=names[i]
    person=list()
    person.append(hname)
    person.append(hs)
    return person
    return person
def low(scores):
    ls=100
    n=len(scores)
    for i in range(n):
        if scores[i]<=ls:
           scores[i]=ls
           lname=names[i]
    person=list()
    person.append(lname)
    person.append(ls)
    return person
def average(scores):
    total=0
    n=len(scores)
    for i in range(n):
        total+=i
        average=total/n
    return average
scores=[]
names=[]
score=0
total=0
people=int(input("幾人?"))
for i in range(people):
    name=input("名字")
    score=int(input("成績"))
    scores.append(score)
    names.append(name)
    print(scores)
    print(names)
print(scores)
print("平均",average(scores),"分")
print("最高",high(scores))
print("最低",low(scores))